# Generated model: Child
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Child(base_cls):
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

    class Child_Current(Child):
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

    class Child_Working(Child):
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
    Child.__undoable_views__ = {'default': Child, 'current': Child_Current, 'working': Child_Working}
    return Child

# Generated model: Parent
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent(base_cls):
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

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def children(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'children' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'children' + ': unresolved constructor field')
                return state.values['children']
            return state.manager._read_managed(self, 'children')

        @children.setter
        def children(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('children' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'children', value)

    class Parent_Current(Parent):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def children(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'children' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'children' + ': unresolved constructor field')
                return state.values['children']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'children')
            return state.manager._committed_value(self, 'children')

        @children.setter
        def children(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('children' + ': current managed facade is read-only')

    class Parent_Working(Parent):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def children(self):
            state = self._u_state
            if self._u_pin is not None or state.constructing or state.manager._selection is None:
                state.manager._require_confirmed()
                if self._u_pin is None and (state.constructing or state.manager._selection is None):
                    if 'children' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'children' + ': unresolved constructor field')
                    return state.values['children']
                return state.manager._read_managed(self, 'children')
            return state.manager._read_managed(self, 'children', allow_thaw=True)

        @children.setter
        def children(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('children' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'children', value)
    Parent.__undoable_views__ = {'default': Parent, 'current': Parent_Current, 'working': Parent_Working}
    return Parent
