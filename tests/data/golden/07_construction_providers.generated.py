# Generated model: Constructed
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Constructed(base_cls):
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

        def __init__(self, *, transaction_manager, doubled=_HAS_DEFAULT_FACTORY, base=_HAS_DEFAULT_FACTORY, derived=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['doubled'] = doubled
            state.inputs['base'] = base
            state.inputs['derived'] = derived
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def doubled(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'doubled' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'doubled' + ': unresolved constructor field')
                return state.values['doubled']
            return state.manager._read_managed(self, 'doubled')

        @doubled.setter
        def doubled(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('doubled' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'doubled', value)

        @property
        def base(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'base' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'base' + ': unresolved constructor field')
                return state.values['base']
            return state.manager._read_managed(self, 'base')

        @base.setter
        def base(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('base' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'base', value)

        @property
        def derived(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'derived' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'derived' + ': unresolved constructor field')
                return state.values['derived']
            return state.manager._read_managed(self, 'derived')

        @derived.setter
        def derived(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('derived' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'derived', value)

    class Constructed_Current(Constructed):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def doubled(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'doubled' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'doubled' + ': unresolved constructor field')
                return state.values['doubled']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'doubled')
            return state.manager._committed_value(self, 'doubled')

        @doubled.setter
        def doubled(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('doubled' + ': current managed facade is read-only')

        @property
        def base(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'base' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'base' + ': unresolved constructor field')
                return state.values['base']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'base')
            return state.manager._committed_value(self, 'base')

        @base.setter
        def base(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('base' + ': current managed facade is read-only')

        @property
        def derived(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'derived' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'derived' + ': unresolved constructor field')
                return state.values['derived']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'derived')
            return state.manager._committed_value(self, 'derived')

        @derived.setter
        def derived(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('derived' + ': current managed facade is read-only')

    class Constructed_Working(Constructed):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def doubled(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'doubled' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'doubled' + ': unresolved constructor field')
                return state.values['doubled']
            return state.manager._read_managed(self, 'doubled')

        @doubled.setter
        def doubled(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('doubled' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'doubled', value)

        @property
        def base(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'base' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'base' + ': unresolved constructor field')
                return state.values['base']
            return state.manager._read_managed(self, 'base')

        @base.setter
        def base(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('base' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'base', value)

        @property
        def derived(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'derived' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'derived' + ': unresolved constructor field')
                return state.values['derived']
            return state.manager._read_managed(self, 'derived')

        @derived.setter
        def derived(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('derived' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'derived', value)
    Constructed.__undoable_views__ = {'default': Constructed, 'current': Constructed_Current, 'working': Constructed_Working}
    return Constructed

# Generated model: ConstructorWrite
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ConstructorWrite(base_cls):
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

        def __init__(self, *, transaction_manager, base=_HAS_DEFAULT_FACTORY, bad=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['base'] = base
            state.inputs['bad'] = bad
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def base(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'base' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'base' + ': unresolved constructor field')
                return state.values['base']
            return state.manager._read_managed(self, 'base')

        @base.setter
        def base(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('base' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'base', value)

        @property
        def bad(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'bad' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'bad' + ': unresolved constructor field')
                return state.values['bad']
            return state.manager._read_managed(self, 'bad')

        @bad.setter
        def bad(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('bad' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'bad', value)

    class ConstructorWrite_Current(ConstructorWrite):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def base(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'base' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'base' + ': unresolved constructor field')
                return state.values['base']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'base')
            return state.manager._committed_value(self, 'base')

        @base.setter
        def base(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('base' + ': current managed facade is read-only')

        @property
        def bad(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'bad' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'bad' + ': unresolved constructor field')
                return state.values['bad']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'bad')
            return state.manager._committed_value(self, 'bad')

        @bad.setter
        def bad(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('bad' + ': current managed facade is read-only')

    class ConstructorWrite_Working(ConstructorWrite):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def base(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'base' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'base' + ': unresolved constructor field')
                return state.values['base']
            return state.manager._read_managed(self, 'base')

        @base.setter
        def base(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('base' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'base', value)

        @property
        def bad(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'bad' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'bad' + ': unresolved constructor field')
                return state.values['bad']
            return state.manager._read_managed(self, 'bad')

        @bad.setter
        def bad(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('bad' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'bad', value)
    ConstructorWrite.__undoable_views__ = {'default': ConstructorWrite, 'current': ConstructorWrite_Current, 'working': ConstructorWrite_Working}
    return ConstructorWrite

# Generated model: Recursive
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Recursive(base_cls):
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

        def __init__(self, *, transaction_manager, a=_HAS_DEFAULT_FACTORY, b=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['a'] = a
            state.inputs['b'] = b
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

    class Recursive_Current(Recursive):
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

    class Recursive_Working(Recursive):
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
    Recursive.__undoable_views__ = {'default': Recursive, 'current': Recursive_Current, 'working': Recursive_Working}
    return Recursive

# Generated model: Unresolved
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Unresolved(base_cls):
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

        def __init__(self, *, transaction_manager, first=_HAS_DEFAULT_FACTORY, later=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['first'] = first
            state.inputs['later'] = later
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def first(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'first' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'first' + ': unresolved constructor field')
                return state.values['first']
            return state.manager._read_managed(self, 'first')

        @first.setter
        def first(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('first' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'first', value)

        @property
        def later(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'later' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'later' + ': unresolved constructor field')
                return state.values['later']
            return state.manager._read_managed(self, 'later')

        @later.setter
        def later(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('later' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'later', value)

    class Unresolved_Current(Unresolved):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def first(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'first' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'first' + ': unresolved constructor field')
                return state.values['first']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'first')
            return state.manager._committed_value(self, 'first')

        @first.setter
        def first(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('first' + ': current managed facade is read-only')

        @property
        def later(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'later' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'later' + ': unresolved constructor field')
                return state.values['later']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'later')
            return state.manager._committed_value(self, 'later')

        @later.setter
        def later(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('later' + ': current managed facade is read-only')

    class Unresolved_Working(Unresolved):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def first(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'first' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'first' + ': unresolved constructor field')
                return state.values['first']
            return state.manager._read_managed(self, 'first')

        @first.setter
        def first(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('first' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'first', value)

        @property
        def later(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'later' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'later' + ': unresolved constructor field')
                return state.values['later']
            return state.manager._read_managed(self, 'later')

        @later.setter
        def later(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('later' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'later', value)
    Unresolved.__undoable_views__ = {'default': Unresolved, 'current': Unresolved_Current, 'working': Unresolved_Working}
    return Unresolved
