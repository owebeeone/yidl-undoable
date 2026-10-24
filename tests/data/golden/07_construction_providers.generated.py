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
            return self._u_read_managed('doubled')

        @doubled.setter
        def doubled(self, value):
            self._u_write_managed('doubled', value)

        @property
        def base(self):
            return self._u_read_managed('base')

        @base.setter
        def base(self, value):
            self._u_write_managed('base', value)

        @property
        def derived(self):
            return self._u_read_managed('derived')

        @derived.setter
        def derived(self, value):
            self._u_write_managed('derived', value)

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
            return self._u_read_current_managed('doubled')

        @doubled.setter
        def doubled(self, value):
            self._u_write_current_managed('doubled', value)

        @property
        def base(self):
            return self._u_read_current_managed('base')

        @base.setter
        def base(self, value):
            self._u_write_current_managed('base', value)

        @property
        def derived(self):
            return self._u_read_current_managed('derived')

        @derived.setter
        def derived(self, value):
            self._u_write_current_managed('derived', value)

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
            return self._u_read_working_managed('doubled')

        @doubled.setter
        def doubled(self, value):
            self._u_write_managed('doubled', value)

        @property
        def base(self):
            return self._u_read_working_managed('base')

        @base.setter
        def base(self, value):
            self._u_write_managed('base', value)

        @property
        def derived(self):
            return self._u_read_working_managed('derived')

        @derived.setter
        def derived(self, value):
            self._u_write_managed('derived', value)
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
            return self._u_read_managed('base')

        @base.setter
        def base(self, value):
            self._u_write_managed('base', value)

        @property
        def bad(self):
            return self._u_read_managed('bad')

        @bad.setter
        def bad(self, value):
            self._u_write_managed('bad', value)

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
            return self._u_read_current_managed('base')

        @base.setter
        def base(self, value):
            self._u_write_current_managed('base', value)

        @property
        def bad(self):
            return self._u_read_current_managed('bad')

        @bad.setter
        def bad(self, value):
            self._u_write_current_managed('bad', value)

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
            return self._u_read_working_managed('base')

        @base.setter
        def base(self, value):
            self._u_write_managed('base', value)

        @property
        def bad(self):
            return self._u_read_working_managed('bad')

        @bad.setter
        def bad(self, value):
            self._u_write_managed('bad', value)
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
            return self._u_read_managed('a')

        @a.setter
        def a(self, value):
            self._u_write_managed('a', value)

        @property
        def b(self):
            return self._u_read_managed('b')

        @b.setter
        def b(self, value):
            self._u_write_managed('b', value)

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
            return self._u_read_current_managed('a')

        @a.setter
        def a(self, value):
            self._u_write_current_managed('a', value)

        @property
        def b(self):
            return self._u_read_current_managed('b')

        @b.setter
        def b(self, value):
            self._u_write_current_managed('b', value)

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
            return self._u_read_working_managed('a')

        @a.setter
        def a(self, value):
            self._u_write_managed('a', value)

        @property
        def b(self):
            return self._u_read_working_managed('b')

        @b.setter
        def b(self, value):
            self._u_write_managed('b', value)
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
            return self._u_read_managed('first')

        @first.setter
        def first(self, value):
            self._u_write_managed('first', value)

        @property
        def later(self):
            return self._u_read_managed('later')

        @later.setter
        def later(self, value):
            self._u_write_managed('later', value)

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
            return self._u_read_current_managed('first')

        @first.setter
        def first(self, value):
            self._u_write_current_managed('first', value)

        @property
        def later(self):
            return self._u_read_current_managed('later')

        @later.setter
        def later(self, value):
            self._u_write_current_managed('later', value)

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
            return self._u_read_working_managed('first')

        @first.setter
        def first(self, value):
            self._u_write_managed('first', value)

        @property
        def later(self):
            return self._u_read_working_managed('later')

        @later.setter
        def later(self, value):
            self._u_write_managed('later', value)
    Unresolved.__undoable_views__ = {'default': Unresolved, 'current': Unresolved_Current, 'working': Unresolved_Working}
    return Unresolved
