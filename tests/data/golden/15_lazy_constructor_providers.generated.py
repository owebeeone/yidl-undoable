# Generated model: Forward
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Forward(base_cls):
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

        def __init__(self, *, transaction_manager, source=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['source'] = source
            state.inputs['constant'] = constant
            state.inputs['value'] = value
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def source(self):
            state = self._u_state
            if 'source' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'source' + ': unresolved constructor field')
            value = state.values['source']
            if value is _u_capture_0.missing:
                if 'source' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'source' + ': recursive lazy provider')
                fact = state.schema.by_name['source']
                state.resolving.add('source')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('source')
                state.values['source'] = value
            return value

        @source.setter
        def source(self, value):
            state = self._u_state
            if state.values['source'] is not _u_capture_0.missing:
                raise AttributeError('source' + ': lazy reference is already initialized')
            state.values['source'] = value

        @property
        def constant(self):
            state = self._u_state
            if 'constant' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'constant' + ': unresolved constructor field')
            return state.values['constant']

        @constant.setter
        def constant(self, value):
            raise AttributeError('constant' + ': const reference is read-only')

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

    class Forward_Current(Forward):
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

    class Forward_Working(Forward):
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
    Forward.__undoable_views__ = {'default': Forward, 'current': Forward_Current, 'working': Forward_Working}
    return Forward

# Generated model: Reverse
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Reverse(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, source=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['constant'] = constant
            state.inputs['source'] = source
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
        def constant(self):
            state = self._u_state
            if 'constant' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'constant' + ': unresolved constructor field')
            return state.values['constant']

        @constant.setter
        def constant(self, value):
            raise AttributeError('constant' + ': const reference is read-only')

        @property
        def source(self):
            state = self._u_state
            if 'source' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'source' + ': unresolved constructor field')
            value = state.values['source']
            if value is _u_capture_0.missing:
                if 'source' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'source' + ': recursive lazy provider')
                fact = state.schema.by_name['source']
                state.resolving.add('source')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('source')
                state.values['source'] = value
            return value

        @source.setter
        def source(self, value):
            state = self._u_state
            if state.values['source'] is not _u_capture_0.missing:
                raise AttributeError('source' + ': lazy reference is already initialized')
            state.values['source'] = value

    class Reverse_Current(Reverse):
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

    class Reverse_Working(Reverse):
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
    Reverse.__undoable_views__ = {'default': Reverse, 'current': Reverse_Current, 'working': Reverse_Working}
    return Reverse
