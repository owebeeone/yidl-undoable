"""Post-GREEN source/bytecode verification of the authored comparison boundary."""

import ast
import dis
import sys
from pathlib import Path
from importlib.resources import files
from yidl_undoable import undoable, managed


@undoable(eq=True, order=True)
class Shape:
    value: int = managed(default=2)
    skipped: int = managed(default=3, compare=False, write_compare="identity")


def test_prelude_precedes_all_self_type_and_value_reads_on_all_facades():
    tree = ast.parse(Shape.__undoable_source__)
    methods = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "__eq__"
    ]
    assert len(methods) == 3
    for method in methods:
        body = method.body
        if (
            isinstance(body[0], ast.If)
            and isinstance(body[0].test, ast.Constant)
            and body[0].test.value is True
        ):
            body = [*body[0].body, *body[1:]]
        assert (
            isinstance(body[0], ast.Assign)
            and body[0].targets[0].id == "_u_write_scope"
        )
        assert (
            body[0].value.func.value.id == "_u_historical_write_scope"
            and body[0].value.func.attr == "get"
        )
        assert (
            isinstance(body[1], ast.If)
            and body[1].body[0].value.func.id == "_u_historical_eq"
        )
        assert not any(
            isinstance(node, ast.Attribute)
            and node.attr in ("__class__", "value", "skipped")
            for node in ast.walk(body[1])
        )
        assert not any(
            isinstance(node, ast.Attribute) and node.attr == "skipped"
            for node in ast.walk(method)
        )
    for view in Shape.__undoable_views__.values():
        assert view.__dict__["__hash__"] is None
        for name in ("__lt__", "__le__", "__gt__", "__ge__"):
            assert (
                "_u_historical_write_scope" not in view.__dict__[name].__code__.co_names
            )


def test_constant_carrier_adds_no_runtime_branch_or_dispatch():
    def reference(self, other):
        _u_write_scope = _u_historical_write_scope.get()
        if _u_write_scope is not None and _u_write_scope.active:
            return _u_historical_eq(self, other)
        return None

    def prefix(function):
        result = []
        for instruction in dis.get_instructions(function):
            if instruction.opname in ("RESUME", "NOP"):
                continue
            if instruction.opname == "RETURN_VALUE":
                return result
            operation = instruction.opname
            if operation in (
                "STORE_FAST_LOAD_FAST",
                "LOAD_FAST_LOAD_FAST",
                "STORE_FAST_STORE_FAST",
                "LOAD_FAST_BORROW_LOAD_FAST_BORROW",
            ):
                operations = (
                    ("STORE_FAST", "LOAD_FAST")
                    if operation == "STORE_FAST_LOAD_FAST"
                    else (
                        ("STORE_FAST", "STORE_FAST")
                        if operation == "STORE_FAST_STORE_FAST"
                        else ("LOAD_FAST", "LOAD_FAST")
                    )
                )
                result.extend(zip(operations, instruction.argval))
            else:
                result.append(
                    (
                        "LOAD_FAST" if operation == "LOAD_FAST_BORROW" else operation,
                        instruction.argval,
                    )
                )

    # Jump byte offsets depend on the structural tail; opcode/name/constant prefix is identical.
    def semantic_prefix(function):
        return [
            (operation, None if "JUMP" in operation else value)
            for operation, value in prefix(function)
        ]

    for view in Shape.__undoable_views__.values():
        assert semantic_prefix(view.__eq__) == semantic_prefix(reference)


def test_shared_authority_and_native_write_expression_have_no_projection_helpers():
    package = files("yidl_undoable")
    source = (package / "write_comparison_context.py").read_text()
    tree = ast.parse(source)
    method = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
    attempt = next(node for node in method.body if isinstance(node, ast.Try))
    expression = attempt.body[0].value
    assert expression.func.id == "bool"
    assert (
        expression.args[0].left.id == "old"
        and expression.args[0].comparators[0].id == "value"
    )
    assert (
        attempt.finalbody[0].targets[0].attr == "active"
        and attempt.finalbody[0].value.value is False
    )
    assert attempt.finalbody[1].value.func.attr == "reset"
    assert not (package / "yidl/shared/comparison.yidl").exists()
    generated = (package / "_generated_undoable_base.py").read_text()
    assert (
        "shared/comparison.yidl sha256=2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef"
        in generated
    )


def test_undoable_scope_does_not_change_dataclass_equality():
    from yidl_dataclass import dataclass, generated_source
    from yidl_undoable.write_comparison_context import _historical_write_equal

    @dataclass
    class Plain:
        value: int

    assert "historical_write" not in generated_source(Plain)
    assert "_u_write_scope" not in Plain.__eq__.__code__.co_names
    left, right = Plain(2), Plain(2)

    class Callback:
        def __eq__(self, other):
            return left == right

    assert _historical_write_equal(Callback(), object()) is True


def test_model_generation_never_imports_dataclass_runtime_authority():
    import subprocess

    script = """import importlib.abc,sys
class Block(importlib.abc.MetaPathFinder):
 def find_spec(self,fullname,path=None,target=None):
  if fullname=="yidl_dataclass" or fullname.startswith("yidl_dataclass."):
   raise AssertionError("Dataclass runtime lookup")
sys.meta_path.insert(0,Block())
from yidl_undoable import undoable,managed,UndoRedoManager
@undoable(eq=True,order=True)
class Model:
 value:int=managed(default=2)
h=UndoRedoManager();a=Model(transaction_manager=h);b=Model(transaction_manager=h);h.initialize(a,b)
assert a==b and a.current==b.current
with h.begin():a.value=3
assert a>b
"""
    import os

    import yidl_undoable

    installed = Path(yidl_undoable.__file__).resolve().is_relative_to(Path(sys.prefix))
    environment = dict(os.environ)
    if installed:
        environment.pop("PYTHONPATH", None)
    else:
        environment["PYTHONPATH"] = str(
            Path(yidl_undoable.__file__).resolve().parent.parent
        )
    result = subprocess.run(
        [sys.executable, *(["-I"] if installed else []), "-c", script],
        capture_output=True,
        text=True,
        env=environment,
    )
    assert result.returncode == 0, result.stderr


def test_multifield_view_hash_slot_keeps_its_public_dunder_name():
    @undoable(eq=True, order=True)
    class RichHash:
        first: int = managed(default=1)
        second: int = managed(default=2)
        third: int = managed(default=3)
        fourth: int = managed(default=4)

    assert "__hash____astichi_scoped" not in RichHash.__undoable_source__
    for view in RichHash.__undoable_views__.values():
        assert view.__dict__.get("__hash__", object()) is None
        assert not any(
            name.startswith("__hash____astichi_scoped") for name in view.__dict__
        )
