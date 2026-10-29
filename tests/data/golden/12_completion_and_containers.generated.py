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

        def __init__(self, *, transaction_manager, data=_HAS_DEFAULT_FACTORY, once=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['data'] = data
            state.inputs['once'] = once
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def data(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'data' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'data' + ': unresolved constructor field')
                return state.values['data']
            return state.manager._read_managed(self, 'data')

        @data.setter
        def data(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('data' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'data', value)

        @property
        def once(self):
            state = self._u_state
            if 'once' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'once' + ': unresolved constructor field')
            value = state.values['once']
            if value is _u_capture_0.missing:
                if 'once' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'once' + ': recursive lazy provider')
                fact = state.schema.by_name['once']
                state.resolving.add('once')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('once')
                state.values['once'] = value
            return value

        @once.setter
        def once(self, value):
            state = self._u_state
            if state.values['once'] is not _u_capture_0.missing:
                raise AttributeError('once' + ': lazy reference is already initialized')
            state.values['once'] = value

    class Lazy_Current(Lazy):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def data(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'data' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'data' + ': unresolved constructor field')
                return state.values['data']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'data')
            return state.manager._committed_value(self, 'data')

        @data.setter
        def data(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('data' + ': current managed facade is read-only')

    class Lazy_Working(Lazy):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def data(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'data' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'data' + ': unresolved constructor field')
                return state.values['data']
            return state.manager._read_managed(self, 'data')

        @data.setter
        def data(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('data' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'data', value)
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

        def __init__(self, *, transaction_manager, values=_HAS_DEFAULT_FACTORY, membership=_HAS_DEFAULT_FACTORY, edges=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['values'] = values
            state.inputs['membership'] = membership
            state.inputs['edges'] = edges
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def values(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'values' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'values' + ': unresolved constructor field')
                return state.values['values']
            return state.manager._read_managed(self, 'values')

        @values.setter
        def values(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('values' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'values', value)

        @property
        def membership(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'membership' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'membership' + ': unresolved constructor field')
                return state.values['membership']
            return state.manager._read_managed(self, 'membership')

        @membership.setter
        def membership(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('membership' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'membership', value)

        @property
        def edges(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'edges' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'edges' + ': unresolved constructor field')
                return state.values['edges']
            return state.manager._read_managed(self, 'edges')

        @edges.setter
        def edges(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('edges' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'edges', value)

    class Node_Current(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def values(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'values' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'values' + ': unresolved constructor field')
                return state.values['values']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'values')
            return state.manager._committed_value(self, 'values')

        @values.setter
        def values(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('values' + ': current managed facade is read-only')

        @property
        def membership(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'membership' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'membership' + ': unresolved constructor field')
                return state.values['membership']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'membership')
            return state.manager._committed_value(self, 'membership')

        @membership.setter
        def membership(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('membership' + ': current managed facade is read-only')

        @property
        def edges(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'edges' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'edges' + ': unresolved constructor field')
                return state.values['edges']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'edges')
            return state.manager._committed_value(self, 'edges')

        @edges.setter
        def edges(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('edges' + ': current managed facade is read-only')

    class Node_Working(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def values(self):
            state = self._u_state
            if self._u_pin is not None or state.constructing or state.manager._selection is None:
                state.manager._require_confirmed()
                if self._u_pin is None and (state.constructing or state.manager._selection is None):
                    if 'values' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'values' + ': unresolved constructor field')
                    return state.values['values']
                return state.manager._read_managed(self, 'values')
            return state.manager._read_managed(self, 'values', allow_thaw=True)

        @values.setter
        def values(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('values' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'values', value)

        @property
        def membership(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'membership' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'membership' + ': unresolved constructor field')
                return state.values['membership']
            return state.manager._read_managed(self, 'membership')

        @membership.setter
        def membership(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('membership' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'membership', value)

        @property
        def edges(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'edges' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'edges' + ': unresolved constructor field')
                return state.values['edges']
            return state.manager._read_managed(self, 'edges')

        @edges.setter
        def edges(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('edges' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'edges', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node
