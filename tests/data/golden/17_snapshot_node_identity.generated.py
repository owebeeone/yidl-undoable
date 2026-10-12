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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY, nested=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['children'] = children
            state.inputs['nested'] = nested
            self._u_finish(state)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

        @property
        def nested(self):
            return self._u_read_managed('nested')

        @nested.setter
        def nested(self, value):
            self._u_write_managed('nested', value)

    class Node_Current(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

        @property
        def nested(self):
            return self._u_read_current_managed('nested')

        @nested.setter
        def nested(self, value):
            self._u_write_current_managed('nested', value)

    class Node_Working(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

        @property
        def nested(self):
            return self._u_read_working_managed('nested')

        @nested.setter
        def nested(self, value):
            self._u_write_managed('nested', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node
