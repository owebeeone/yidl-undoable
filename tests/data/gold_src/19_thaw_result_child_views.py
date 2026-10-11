from yidl_undoable import *


@undoable
class Child:
    value: int = managed(default=0)
    items: tuple = managed(default=(), thaw=list, freeze=tuple)


output_view = "default"


def thaw_children(children):
    return [
        {"child": getattr(child, output_view), "aliases": {getattr(child, output_view)}}
        for child in children
    ]


@undoable
class Parent:
    children: tuple = managed(
        default=(),
        thaw=thaw_children,
        freeze=lambda rows: tuple(
            row["child"] if type(row) is dict else row for row in rows
        ),
    )


for output_view in ("default", "current"):
    for provisional in (False, True):
        h = UndoRedoManager()
        child = Child(transaction_manager=h)
        parent = (
            None if provisional else Parent(children=(child,), transaction_manager=h)
        )
        h.initialize(child) if provisional else h.initialize(child, parent)
        with h.begin():
            child.value = 7
            if provisional:
                parent = Parent(children=(child,), transaction_manager=h)
                h.add_root(parent)
            assert parent.children[0] is child.default
            assert parent.children[0].items == ()
            assert (child.node_id, "items") not in h._edit.touched
            first = parent.working.children
            row, aliases = first[0], first[0]["aliases"]
            assert (
                row["child"] is child.working and next(iter(aliases)) is child.working
            )
            assert row["child"].value == 7
            row["child"].items.append("first")
            second = parent.working.children
            assert (
                second is first and second[0] is row and second[0]["aliases"] is aliases
            )
            ordinary = parent.children
            assert ordinary[0]["child"] is child.default
            assert next(iter(ordinary[0]["aliases"])) is child.default
            assert row["child"] is child.working
        assert parent.children[0] is child.default
        assert child.items == ("first",) and child.value == 7
