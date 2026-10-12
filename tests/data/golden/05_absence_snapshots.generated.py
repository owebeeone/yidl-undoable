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

        def __init__(self, *, transaction_manager, number=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['number'] = number
            state.inputs['children'] = children
            state.inputs['resource'] = resource
            self._u_finish(state)

        @property
        def number(self):
            return self._u_read_managed('number')

        @number.setter
        def number(self, value):
            self._u_write_managed('number', value)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

        @property
        def resource(self):
            return self._u_read_plain('resource')

        @resource.setter
        def resource(self, value):
            self._u_write_plain('resource', value)

    class Node_Current(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def number(self):
            return self._u_read_current_managed('number')

        @number.setter
        def number(self, value):
            self._u_write_current_managed('number', value)

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
        def number(self):
            return self._u_read_working_managed('number')

        @number.setter
        def number(self, value):
            self._u_write_managed('number', value)

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node
