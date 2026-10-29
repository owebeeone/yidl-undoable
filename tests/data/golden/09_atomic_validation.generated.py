# Generated model: Checked
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Checked(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, valid=_HAS_DEFAULT_FACTORY, attack=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['valid'] = valid
            state.inputs['attack'] = attack
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

        @property
        def valid(self):
            state = self._u_state
            if 'valid' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'valid' + ': unresolved constructor field')
            return state.values['valid']

        @valid.setter
        def valid(self, value):
            self._u_state.values['valid'] = value

        @property
        def seen(self):
            state = self._u_state
            if 'seen' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'seen' + ': unresolved constructor field')
            return state.values['seen']

        @seen.setter
        def seen(self, value):
            self._u_state.values['seen'] = value

        @property
        def attack(self):
            state = self._u_state
            if 'attack' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'attack' + ': unresolved constructor field')
            return state.values['attack']

        @attack.setter
        def attack(self, value):
            self._u_state.values['attack'] = value

    class Checked_Current(Checked):
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

    class Checked_Working(Checked):
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
    Checked.__undoable_views__ = {'default': Checked, 'current': Checked_Current, 'working': Checked_Working}
    return Checked

# Generated model: Frozen
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Frozen(base_cls):
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

        def __init__(self, *, transaction_manager, data=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['data'] = data
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

    class Frozen_Current(Frozen):
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

    class Frozen_Working(Frozen):
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
    Frozen.__undoable_views__ = {'default': Frozen, 'current': Frozen_Current, 'working': Frozen_Working}
    return Frozen

# Generated model: MappingNode
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class MappingNode(base_cls):
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

        def __init__(self, *, transaction_manager, mapping=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['mapping'] = mapping
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def mapping(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'mapping' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'mapping' + ': unresolved constructor field')
                return state.values['mapping']
            return state.manager._read_managed(self, 'mapping')

        @mapping.setter
        def mapping(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('mapping' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'mapping', value)

    class MappingNode_Current(MappingNode):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def mapping(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'mapping' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'mapping' + ': unresolved constructor field')
                return state.values['mapping']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'mapping')
            return state.manager._committed_value(self, 'mapping')

        @mapping.setter
        def mapping(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('mapping' + ': current managed facade is read-only')

    class MappingNode_Working(MappingNode):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def mapping(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'mapping' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'mapping' + ': unresolved constructor field')
                return state.values['mapping']
            return state.manager._read_managed(self, 'mapping')

        @mapping.setter
        def mapping(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('mapping' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'mapping', value)
    MappingNode.__undoable_views__ = {'default': MappingNode, 'current': MappingNode_Current, 'working': MappingNode_Working}
    return MappingNode
