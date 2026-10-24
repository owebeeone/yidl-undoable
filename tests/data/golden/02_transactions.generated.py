# Generated model: Item
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Item(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, sequence=_HAS_DEFAULT_FACTORY, plain=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['sequence'] = sequence
            state.inputs['plain'] = plain
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def sequence(self):
            return self._u_read_managed('sequence')

        @sequence.setter
        def sequence(self, value):
            self._u_write_managed('sequence', value)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

    class Item_Current(Item):
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
        def sequence(self):
            return self._u_read_current_managed('sequence')

        @sequence.setter
        def sequence(self, value):
            self._u_write_current_managed('sequence', value)

    class Item_Working(Item):
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
        def sequence(self):
            return self._u_read_thaw_managed('sequence')

        @sequence.setter
        def sequence(self, value):
            self._u_write_managed('sequence', value)
    Item.__undoable_views__ = {'default': Item, 'current': Item_Current, 'working': Item_Working}
    return Item
