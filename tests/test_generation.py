from pathlib import Path
import ast
from yidl_undoable import undoable, managed, lazy, transient
from yidl_undoable.regenerate_undoable_base import check_undoable_base


@undoable
class Selected:
    required: int = managed()
    defaulted: int = managed(default=1)
    factory: tuple = managed(default_factory=tuple)
    scratch: list = transient(default_factory=list, working_default_factory=list)
    fixed_lazy: int = lazy(default=2)
    mutable_lazy: int = lazy(default_factory=int, mutable=True)


def test_matcher_selected_executable_surface():
    tree = ast.parse(Selected.__undoable_source__)
    classes = [n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
    assert len(classes) == 3
    assert "_u_read_current_managed" in Selected.__undoable_source__
    assert "_u_read_working_managed" in Selected.__undoable_source__
    assert "_u_write_mutable_static" in Selected.__undoable_source__
    assert "_u_read_factory_static" in Selected.__undoable_source__
    assert "_u_read_factory_transient" in Selected.__undoable_source__
    assert check_undoable_base() == (True, "")


def test_resource_regeneration_is_independent_of_install_layout(tmp_path):
    import shutil
    import yidl_undoable
    from yidl_undoable.regenerate_undoable_base import render_undoable_base_source

    original = Path(yidl_undoable.__file__).parent / "yidl"
    copied = tmp_path / "different" / "resources"
    shutil.copytree(original, copied)
    assert (
        render_undoable_base_source(
            source_dir=copied,
            entry_path=copied / "undoable_base.yidl",
            project_root=tmp_path,
        )
        == render_undoable_base_source()
    )
