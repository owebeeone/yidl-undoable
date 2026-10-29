# Generated model: Lazy
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Lazy(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['delayed'] = delayed
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
        def delayed(self):
            state = self._u_state
            if 'delayed' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'delayed' + ': unresolved constructor field')
            value = state.values['delayed']
            if value is _u_capture_0.missing:
                if 'delayed' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'delayed' + ': recursive lazy provider')
                fact = state.schema.by_name['delayed']
                state.resolving.add('delayed')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('delayed')
                state.values['delayed'] = value
            return value

        @delayed.setter
        def delayed(self, value):
            state = self._u_state
            if state.values['delayed'] is not _u_capture_0.missing:
                raise AttributeError('delayed' + ': lazy reference is already initialized')
            state.values['delayed'] = value

    class Lazy_Current(Lazy):
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

    class Lazy_Working(Lazy):
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
    Lazy.__undoable_views__ = {'default': Lazy, 'current': Lazy_Current, 'working': Lazy_Working}
    return Lazy

# Generated model: Node
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Node(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['items'] = items
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

    class Node_Current(Node):
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

    class Node_Working(Node):
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
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node

# Generated model: Scratch
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Scratch(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['scratch'] = scratch
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
        def scratch(self):
            state = self._u_state
            if state.constructing:
                if 'scratch' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'scratch' + ': unresolved constructor field')
                return state.values['scratch']
            edit = state.manager._edit
            historical_pin = self._u_pin is not None and (not isinstance(self._u_pin, _u_capture_0.candidate_type))
            if edit is None or self._u_view == 'current' or historical_pin:
                if 'scratch' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'scratch' + ': unresolved constructor field')
                return state.values['scratch']
            key = (state.node_id, 'scratch')
            if key not in edit.transient:
                if 'scratch' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'scratch' + ': recursive transient provider')
                state.resolving.add('scratch')
                try:
                    value = None
                    fact = state.schema.by_name['scratch']
                    value = self._u_factory(fact, 'working_default')
                finally:
                    state.resolving.remove('scratch')
                edit.transient[key] = value
            return edit.transient[key]

        @scratch.setter
        def scratch(self, value):
            edit = self._u_state.manager._require_edit()
            if self._u_view == 'current' or self._u_pin is not None:
                raise _u_capture_0.transaction_error('current transient facade is read-only')
            edit.transient[self.node_id, 'scratch'] = value

    class Scratch_Current(Scratch):
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

    class Scratch_Working(Scratch):
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
    Scratch.__undoable_views__ = {'default': Scratch, 'current': Scratch_Current, 'working': Scratch_Working}
    return Scratch
