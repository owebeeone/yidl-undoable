# Generated model: ClassOnly
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ClassOnly(base_cls):
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
        label = schema.by_name['label']['default_value']

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}
        pass

    class ClassOnly_Current(ClassOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class ClassOnly_Working(ClassOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    ClassOnly.__undoable_views__ = {'default': ClassOnly, 'current': ClassOnly_Current, 'working': ClassOnly_Working}
    return ClassOnly

# Generated model: Empty
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Empty(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}
        pass

    class Empty_Current(Empty):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class Empty_Working(Empty):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    Empty.__undoable_views__ = {'default': Empty, 'current': Empty_Current, 'working': Empty_Working}
    return Empty

# Generated model: NoInputs
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class NoInputs(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
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

    class NoInputs_Current(NoInputs):
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

    class NoInputs_Working(NoInputs):
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
    NoInputs.__undoable_views__ = {'default': NoInputs, 'current': NoInputs_Current, 'working': NoInputs_Working}
    return NoInputs

# Generated model: ScratchOnly
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ScratchOnly(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def cache(self):
            state = self._u_state
            if 'cache' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'cache' + ': unresolved constructor field')
            return state.values['cache']

        @cache.setter
        def cache(self, value):
            self._u_state.values['cache'] = value

    class ScratchOnly_Current(ScratchOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class ScratchOnly_Working(ScratchOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    ScratchOnly.__undoable_views__ = {'default': ScratchOnly, 'current': ScratchOnly_Current, 'working': ScratchOnly_Working}
    return ScratchOnly

# Generated model: kind
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class NoInputs(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
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

    class NoInputs_Current(NoInputs):
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

    class NoInputs_Working(NoInputs):
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
    NoInputs.__undoable_views__ = {'default': NoInputs, 'current': NoInputs_Current, 'working': NoInputs_Working}
    return NoInputs
