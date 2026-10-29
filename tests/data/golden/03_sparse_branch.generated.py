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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'a' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'a' + ': unresolved constructor field')
                return state.values['a']
            return state.manager._read_managed(self, 'a')

        @a.setter
        def a(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('a' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'a', value)

        @property
        def b(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'b' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'b' + ': unresolved constructor field')
                return state.values['b']
            return state.manager._read_managed(self, 'b')

        @b.setter
        def b(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('b' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'b', value)

        @property
        def items(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'items' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'items' + ': unresolved constructor field')
                return state.values['items']
            return state.manager._read_managed(self, 'items')

        @items.setter
        def items(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('items' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'items', value)

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
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'a' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'a' + ': unresolved constructor field')
                return state.values['a']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'a')
            return state.manager._committed_value(self, 'a')

        @a.setter
        def a(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('a' + ': current managed facade is read-only')

        @property
        def b(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'b' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'b' + ': unresolved constructor field')
                return state.values['b']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'b')
            return state.manager._committed_value(self, 'b')

        @b.setter
        def b(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('b' + ': current managed facade is read-only')

        @property
        def items(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'items' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'items' + ': unresolved constructor field')
                return state.values['items']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'items')
            return state.manager._committed_value(self, 'items')

        @items.setter
        def items(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('items' + ': current managed facade is read-only')

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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'a' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'a' + ': unresolved constructor field')
                return state.values['a']
            return state.manager._read_managed(self, 'a')

        @a.setter
        def a(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('a' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'a', value)

        @property
        def b(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'b' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'b' + ': unresolved constructor field')
                return state.values['b']
            return state.manager._read_managed(self, 'b')

        @b.setter
        def b(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('b' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'b', value)

        @property
        def items(self):
            state = self._u_state
            if self._u_pin is not None or state.constructing or state.manager._selection is None:
                state.manager._require_confirmed()
                if self._u_pin is None and (state.constructing or state.manager._selection is None):
                    if 'items' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'items' + ': unresolved constructor field')
                    return state.values['items']
                return state.manager._read_managed(self, 'items')
            return state.manager._read_managed(self, 'items', allow_thaw=True)

        @items.setter
        def items(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('items' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'items', value)
    Pair.__undoable_views__ = {'default': Pair, 'current': Pair_Current, 'working': Pair_Working}
    return Pair
