# Generated model: Node
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Node(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY, mapping=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['children'] = children
            state.inputs['mapping'] = mapping
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
        def mapping(self):
            return self._u_read_managed('mapping')

        @mapping.setter
        def mapping(self, value):
            self._u_write_managed('mapping', value)

    class Node_Current(Node):
        __slots__ = ()

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
        def mapping(self):
            return self._u_read_current_managed('mapping')

        @mapping.setter
        def mapping(self, value):
            self._u_write_current_managed('mapping', value)

    class Node_Working(Node):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def children(self):
            return self._u_read_thaw_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

        @property
        def mapping(self):
            return self._u_read_working_managed('mapping')

        @mapping.setter
        def mapping(self, value):
            self._u_write_managed('mapping', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node

# Generated model: Parent
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['children'] = children
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

    class Parent_Current(Parent):
        __slots__ = ()

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

    class Parent_Working(Parent):
        __slots__ = ()

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
    Parent.__undoable_views__ = {'default': Parent, 'current': Parent_Current, 'working': Parent_Working}
    return Parent

# Generated model: Providers
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Providers(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, x=_HAS_DEFAULT_FACTORY, a=_HAS_DEFAULT_FACTORY, b=_HAS_DEFAULT_FACTORY, recursive=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['x'] = x
            state.inputs['a'] = a
            state.inputs['b'] = b
            state.inputs['recursive'] = recursive
            self._u_finish(state)

        @property
        def x(self):
            return self._u_read_managed('x')

        @x.setter
        def x(self, value):
            self._u_write_managed('x', value)

        @property
        def a(self):
            return self._u_read_factory_static('a')

        @a.setter
        def a(self, value):
            self._u_write_once_static('a', value)

        @property
        def b(self):
            return self._u_read_factory_static('b')

        @b.setter
        def b(self, value):
            self._u_write_once_static('b', value)

        @property
        def recursive(self):
            return self._u_read_factory_static('recursive')

        @recursive.setter
        def recursive(self, value):
            self._u_write_once_static('recursive', value)

    class Providers_Current(Providers):
        __slots__ = ()

        @property
        def x(self):
            return self._u_read_current_managed('x')

        @x.setter
        def x(self, value):
            self._u_write_current_managed('x', value)

    class Providers_Working(Providers):
        __slots__ = ()

        @property
        def x(self):
            return self._u_read_working_managed('x')

        @x.setter
        def x(self, value):
            self._u_write_managed('x', value)
    Providers.__undoable_views__ = {'default': Providers, 'current': Providers_Current, 'working': Providers_Working}
    return Providers

# Generated model: Scratch
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Scratch(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, x=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['x'] = x
            state.inputs['scratch'] = scratch
            self._u_finish(state)

        @property
        def x(self):
            return self._u_read_managed('x')

        @x.setter
        def x(self, value):
            self._u_write_managed('x', value)

        @property
        def scratch(self):
            return self._u_read_factory_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

    class Scratch_Current(Scratch):
        __slots__ = ()

        @property
        def x(self):
            return self._u_read_current_managed('x')

        @x.setter
        def x(self, value):
            self._u_write_current_managed('x', value)

    class Scratch_Working(Scratch):
        __slots__ = ()

        @property
        def x(self):
            return self._u_read_working_managed('x')

        @x.setter
        def x(self, value):
            self._u_write_managed('x', value)
    Scratch.__undoable_views__ = {'default': Scratch, 'current': Scratch_Current, 'working': Scratch_Working}
    return Scratch
