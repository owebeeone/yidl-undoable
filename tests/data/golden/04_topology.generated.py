# Generated model: Node
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Node(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, label=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['label'] = label
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def label(self):
            return self._u_read_managed('label')

        @label.setter
        def label(self, value):
            self._u_write_managed('label', value)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Node_Current(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def label(self):
            return self._u_read_current_managed('label')

        @label.setter
        def label(self, value):
            self._u_write_current_managed('label', value)

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Node_Working(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def label(self):
            return self._u_read_working_managed('label')

        @label.setter
        def label(self, value):
            self._u_write_managed('label', value)

        @property
        def children(self):
            return self._u_read_thaw_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node
