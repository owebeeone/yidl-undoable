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

        def __init__(self, *, transaction_manager, required, payload=_HAS_DEFAULT_FACTORY, seed=_HAS_DEFAULT_FACTORY, label=_HAS_DEFAULT_FACTORY, count=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['required'] = required
            state.inputs['payload'] = payload
            state.inputs['seed'] = seed
            state.inputs['label'] = label
            state.inputs['count'] = count
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def required(self):
            state = self._u_state
            if 'required' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'required' + ': unresolved constructor field')
            return state.values['required']

        @required.setter
        def required(self, value):
            raise AttributeError('required' + ': const reference is read-only')

        @property
        def payload(self):
            state = self._u_state
            if 'payload' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'payload' + ': unresolved constructor field')
            return state.values['payload']

        @payload.setter
        def payload(self, value):
            raise AttributeError('payload' + ': const reference is read-only')

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def label(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'label' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'label' + ': unresolved constructor field')
                return state.values['label']
            return state.manager._read_managed(self, 'label')

        @label.setter
        def label(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('label' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'label', value)

        @property
        def count(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'count' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'count' + ': unresolved constructor field')
                return state.values['count']
            return state.manager._read_managed(self, 'count')

        @count.setter
        def count(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('count' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'count', value)

    class Model_Current(Model):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def label(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'label' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'label' + ': unresolved constructor field')
                return state.values['label']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'label')
            return state.manager._committed_value(self, 'label')

        @label.setter
        def label(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('label' + ': current managed facade is read-only')

        @property
        def count(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'count' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'count' + ': unresolved constructor field')
                return state.values['count']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'count')
            return state.manager._committed_value(self, 'count')

        @count.setter
        def count(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('count' + ': current managed facade is read-only')

    class Model_Working(Model):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def label(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'label' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'label' + ': unresolved constructor field')
                return state.values['label']
            return state.manager._read_managed(self, 'label')

        @label.setter
        def label(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('label' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'label', value)

        @property
        def count(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'count' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'count' + ': unresolved constructor field')
                return state.values['count']
            return state.manager._read_managed(self, 'count')

        @count.setter
        def count(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('count' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'count', value)
    Model.__undoable_views__ = {'default': Model, 'current': Model_Current, 'working': Model_Working}
    return Model
