from yidl_undoable import undoable, managed, const, local_store, UndoRedoManager


@undoable
class Node:
    label: str = managed(default="")
    children: tuple = managed(default=(), thaw=list, freeze=tuple)
    identifier: str = const()
    cache: dict = local_store(default_factory=dict)


history = UndoRedoManager()
root = Node(identifier="root", transaction_manager=history)
assert root.label == ""
assert root.default is root
history.initialize(root)
assert history.cursor == 0 and history.frame_id == 0 and history.frame_count == 1
assert root.present and root.children == ()
assert history.roots == (root,)
assert root.current.label == root.working.label == ""
assert root.cache is root.current.cache
assert "def build_undoable_class" in Node.__undoable_source__
assert "def label" in Node.__undoable_source__
