# Generated model: Lazy
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Lazy(base_cls):
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

        def __init__(self, *, transaction_manager, data=_HAS_DEFAULT_FACTORY, once=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['data'] = data
            state.inputs['once'] = once
            self._u_finish(state)

        @property
        def data(self):
            return self._u_read_managed('data')

        @data.setter
        def data(self, value):
            self._u_write_managed('data', value)

        @property
        def once(self):
            return self._u_read_factory_static('once')

        @once.setter
        def once(self, value):
            self._u_write_once_static('once', value)

    class Lazy_Current(Lazy):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def data(self):
            return self._u_read_current_managed('data')

        @data.setter
        def data(self, value):
            self._u_write_current_managed('data', value)

    class Lazy_Working(Lazy):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def data(self):
            return self._u_read_working_managed('data')

        @data.setter
        def data(self, value):
            self._u_write_managed('data', value)
    Lazy.__undoable_views__ = {'default': Lazy, 'current': Lazy_Current, 'working': Lazy_Working}
    return Lazy

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

        def __init__(self, *, transaction_manager, values=_HAS_DEFAULT_FACTORY, membership=_HAS_DEFAULT_FACTORY, edges=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['values'] = values
            state.inputs['membership'] = membership
            state.inputs['edges'] = edges
            self._u_finish(state)

        @property
        def values(self):
            return self._u_read_managed('values')

        @values.setter
        def values(self, value):
            self._u_write_managed('values', value)

        @property
        def membership(self):
            return self._u_read_managed('membership')

        @membership.setter
        def membership(self, value):
            self._u_write_managed('membership', value)

        @property
        def edges(self):
            return self._u_read_managed('edges')

        @edges.setter
        def edges(self, value):
            self._u_write_managed('edges', value)

    class Node_Current(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def values(self):
            return self._u_read_current_managed('values')

        @values.setter
        def values(self, value):
            self._u_write_current_managed('values', value)

        @property
        def membership(self):
            return self._u_read_current_managed('membership')

        @membership.setter
        def membership(self, value):
            self._u_write_current_managed('membership', value)

        @property
        def edges(self):
            return self._u_read_current_managed('edges')

        @edges.setter
        def edges(self, value):
            self._u_write_current_managed('edges', value)

    class Node_Working(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def values(self):
            return self._u_read_thaw_managed('values')

        @values.setter
        def values(self, value):
            self._u_write_managed('values', value)

        @property
        def membership(self):
            return self._u_read_working_managed('membership')

        @membership.setter
        def membership(self, value):
            self._u_write_managed('membership', value)

        @property
        def edges(self):
            return self._u_read_working_managed('edges')

        @edges.setter
        def edges(self, value):
            self._u_write_managed('edges', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node
