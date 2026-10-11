# Generated model: Child
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Child(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['items'] = items
            self._u_finish(state)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def items(self):
            return self._u_read_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)

    class Child_Current(Child):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def items(self):
            return self._u_read_current_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_current_managed('items', value)

    class Child_Working(Child):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def items(self):
            return self._u_read_thaw_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)
    Child.__undoable_views__ = {'default': Child, 'current': Child_Current, 'working': Child_Working}
    return Child

# Generated model: Parent
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_Current(Parent):
        __slots__ = ()

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_Working(Parent):
        __slots__ = ()

        @property
        def children(self):
            return self._u_read_thaw_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent.__undoable_views__ = {'default': Parent, 'current': Parent_Current, 'working': Parent_Working}
    return Parent
