# Generated model: Model
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Model(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, temporary=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['temporary'] = temporary
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
        def temporary(self):
            state = self._u_state
            if state.constructing:
                if 'temporary' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                return state.values['temporary']
            edit = state.manager._edit
            historical_pin = self._u_pin is not None and (not isinstance(self._u_pin, _u_capture_0.candidate_type))
            if edit is None or self._u_view == 'current' or historical_pin:
                if 'temporary' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                return state.values['temporary']
            key = (state.node_id, 'temporary')
            if key not in edit.transient:
                if 'temporary' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': recursive transient provider')
                state.resolving.add('temporary')
                try:
                    value = None
                    if 'temporary' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                    value = state.values['temporary']
                finally:
                    state.resolving.remove('temporary')
                edit.transient[key] = value
            return edit.transient[key]

        @temporary.setter
        def temporary(self, value):
            edit = self._u_state.manager._require_edit()
            if self._u_view == 'current' or self._u_pin is not None:
                raise _u_capture_0.transaction_error('current transient facade is read-only')
            edit.transient[self.node_id, 'temporary'] = value

    class Model_Current(Model):
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

    class Model_Working(Model):
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
    Model.__undoable_views__ = {'default': Model, 'current': Model_Current, 'working': Model_Working}
    return Model
