# Generated model: Pair
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Pair(base_cls):
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

        def __init__(self, *, transaction_manager, a=_HAS_DEFAULT_FACTORY, b=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['a'] = a
            state.inputs['b'] = b
            state.inputs['items'] = items
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def a(self):
            return self._u_read_managed('a')

        @a.setter
        def a(self, value):
            self._u_write_managed('a', value)

        @property
        def b(self):
            return self._u_read_managed('b')

        @b.setter
        def b(self, value):
            self._u_write_managed('b', value)

        @property
        def items(self):
            return self._u_read_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)

    class Pair_Current(Pair):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def a(self):
            return self._u_read_current_managed('a')

        @a.setter
        def a(self, value):
            self._u_write_current_managed('a', value)

        @property
        def b(self):
            return self._u_read_current_managed('b')

        @b.setter
        def b(self, value):
            self._u_write_current_managed('b', value)

        @property
        def items(self):
            return self._u_read_current_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_current_managed('items', value)

    class Pair_Working(Pair):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def a(self):
            return self._u_read_working_managed('a')

        @a.setter
        def a(self, value):
            self._u_write_managed('a', value)

        @property
        def b(self):
            return self._u_read_working_managed('b')

        @b.setter
        def b(self, value):
            self._u_write_managed('b', value)

        @property
        def items(self):
            return self._u_read_thaw_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)
    Pair.__undoable_views__ = {'default': Pair, 'current': Pair_Current, 'working': Pair_Working}
    return Pair
