"""Runnable companion to docs/Initialization.md."""

from yidl_undoable import UndoRedoManager, initvar, lazy, managed, undoable

@undoable
class Rectangle:
    area: int = managed(default_factory=lambda width, height: width * height)
    width: int = managed(default=3)
    height: int = managed(default=4)
    scale: int = initvar(default=2)
    scaled_area: int = lazy(default_factory=lambda area, scale: area * scale)

history = UndoRedoManager()
rectangle = Rectangle(width=5, transaction_manager=history)
history.initialize(rectangle)
assert rectangle.area == 20 and rectangle.scaled_area == 40
assert not hasattr(rectangle, "scale")
