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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)

        @property
        def sequence(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'sequence' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'sequence' + ': unresolved constructor field')
                return state.values['sequence']
            return state.manager._read_managed(self, 'sequence')

        @sequence.setter
        def sequence(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('sequence' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'sequence', value)

        @property
        def plain(self):
            state = self._u_state
            if 'plain' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'plain' + ': unresolved constructor field')
            return state.values['plain']

        @plain.setter
        def plain(self, value):
            self._u_state.values['plain'] = value

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
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'value')
            return state.manager._committed_value(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('value' + ': current managed facade is read-only')

        @property
        def sequence(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'sequence' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'sequence' + ': unresolved constructor field')
                return state.values['sequence']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'sequence')
            return state.manager._committed_value(self, 'sequence')

        @sequence.setter
        def sequence(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('sequence' + ': current managed facade is read-only')

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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)

        @property
        def sequence(self):
            state = self._u_state
            if self._u_pin is not None or state.constructing or state.manager._selection is None:
                state.manager._require_confirmed()
                if self._u_pin is None and (state.constructing or state.manager._selection is None):
                    if 'sequence' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'sequence' + ': unresolved constructor field')
                    return state.values['sequence']
                return state.manager._read_managed(self, 'sequence')
            return state.manager._read_managed(self, 'sequence', allow_thaw=True)

        @sequence.setter
        def sequence(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('sequence' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'sequence', value)
    Item.__undoable_views__ = {'default': Item, 'current': Item_Current, 'working': Item_Working}
    return Item
