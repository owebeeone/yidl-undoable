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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY, mapping=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['children'] = children
            state.inputs['mapping'] = mapping
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
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node

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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['children'] = children
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
    Parent.__undoable_views__ = {'default': Parent, 'current': Parent_Current, 'working': Parent_Working}
    return Parent

# Generated model: Providers
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Providers(base_cls):
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

        def __init__(self, *, transaction_manager, x=_HAS_DEFAULT_FACTORY, a=_HAS_DEFAULT_FACTORY, b=_HAS_DEFAULT_FACTORY, recursive=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['x'] = x
            state.inputs['a'] = a
            state.inputs['b'] = b
            state.inputs['recursive'] = recursive
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def x(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'x' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'x' + ': unresolved constructor field')
                return state.values['x']
            return state.manager._read_managed(self, 'x')

        @x.setter
        def x(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('x' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'x', value)

        @property
        def a(self):
            state = self._u_state
            if 'a' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'a' + ': unresolved constructor field')
            value = state.values['a']
            if value is _u_capture_0.missing:
                if 'a' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'a' + ': recursive lazy provider')
                fact = state.schema.by_name['a']
                state.resolving.add('a')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('a')
                state.values['a'] = value
            return value

        @a.setter
        def a(self, value):
            state = self._u_state
            if state.values['a'] is not _u_capture_0.missing:
                raise AttributeError('a' + ': lazy reference is already initialized')
            state.values['a'] = value

        @property
        def b(self):
            state = self._u_state
            if 'b' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'b' + ': unresolved constructor field')
            value = state.values['b']
            if value is _u_capture_0.missing:
                if 'b' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'b' + ': recursive lazy provider')
                fact = state.schema.by_name['b']
                state.resolving.add('b')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('b')
                state.values['b'] = value
            return value

        @b.setter
        def b(self, value):
            state = self._u_state
            if state.values['b'] is not _u_capture_0.missing:
                raise AttributeError('b' + ': lazy reference is already initialized')
            state.values['b'] = value

        @property
        def recursive(self):
            state = self._u_state
            if 'recursive' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'recursive' + ': unresolved constructor field')
            value = state.values['recursive']
            if value is _u_capture_0.missing:
                if 'recursive' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'recursive' + ': recursive lazy provider')
                fact = state.schema.by_name['recursive']
                state.resolving.add('recursive')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('recursive')
                state.values['recursive'] = value
            return value

        @recursive.setter
        def recursive(self, value):
            state = self._u_state
            if state.values['recursive'] is not _u_capture_0.missing:
                raise AttributeError('recursive' + ': lazy reference is already initialized')
            state.values['recursive'] = value

    class Providers_Current(Providers):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def x(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'x' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'x' + ': unresolved constructor field')
                return state.values['x']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'x')
            return state.manager._committed_value(self, 'x')

        @x.setter
        def x(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('x' + ': current managed facade is read-only')

    class Providers_Working(Providers):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def x(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'x' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'x' + ': unresolved constructor field')
                return state.values['x']
            return state.manager._read_managed(self, 'x')

        @x.setter
        def x(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('x' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'x', value)
    Providers.__undoable_views__ = {'default': Providers, 'current': Providers_Current, 'working': Providers_Working}
    return Providers

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

        def __init__(self, *, transaction_manager, x=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['x'] = x
            state.inputs['scratch'] = scratch
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def x(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'x' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'x' + ': unresolved constructor field')
                return state.values['x']
            return state.manager._read_managed(self, 'x')

        @x.setter
        def x(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('x' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'x', value)

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
        def x(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'x' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'x' + ': unresolved constructor field')
                return state.values['x']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'x')
            return state.manager._committed_value(self, 'x')

        @x.setter
        def x(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('x' + ': current managed facade is read-only')

    class Scratch_Working(Scratch):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def x(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'x' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'x' + ': unresolved constructor field')
                return state.values['x']
            return state.manager._read_managed(self, 'x')

        @x.setter
        def x(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('x' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'x', value)
    Scratch.__undoable_views__ = {'default': Scratch, 'current': Scratch_Current, 'working': Scratch_Working}
    return Scratch
