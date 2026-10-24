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
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

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
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

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
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent.__undoable_views__ = {'default': Parent, 'current': Parent_Current, 'working': Parent_Working}
    return Parent

# Generated model: _u_capture_0
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_Current(_u_capture_0):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_Working(_u_capture_0):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0.__undoable_views__ = {'default': _u_capture_0, 'current': _u_capture_0_Current, 'working': _u_capture_0_Working}
    return _u_capture_0

# Generated model: _u_capture_0_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_1.equal
        __hash__ = _u_capture_1.hash_function
        __lt__ = _u_capture_1.less
        __le__ = _u_capture_1.less_equal
        __gt__ = _u_capture_1.greater
        __ge__ = _u_capture_1.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_Current(_u_capture_0):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_Working(_u_capture_0):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0.__undoable_views__ = {'default': _u_capture_0, 'current': _u_capture_0_Current, 'working': _u_capture_0_Working}
    return _u_capture_0

# Generated model: _u_capture_0_current
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_current(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_current_Current(_u_capture_0_current):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_current_Working(_u_capture_0_current):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_current.__undoable_views__ = {'default': _u_capture_0_current, 'current': _u_capture_0_current_Current, 'working': _u_capture_0_current_Working}
    return _u_capture_0_current

# Generated model: _u_capture_0_current_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_current(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_1.equal
        __hash__ = _u_capture_1.hash_function
        __lt__ = _u_capture_1.less
        __le__ = _u_capture_1.less_equal
        __gt__ = _u_capture_1.greater
        __ge__ = _u_capture_1.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_current_Current(_u_capture_0_current):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_current_Working(_u_capture_0_current):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_current.__undoable_views__ = {'default': _u_capture_0_current, 'current': _u_capture_0_current_Current, 'working': _u_capture_0_current_Working}
    return _u_capture_0_current

# Generated model: _u_capture_0_default
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_default(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_default_Current(_u_capture_0_default):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_default_Working(_u_capture_0_default):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_default.__undoable_views__ = {'default': _u_capture_0_default, 'current': _u_capture_0_default_Current, 'working': _u_capture_0_default_Working}
    return _u_capture_0_default

# Generated model: _u_capture_0_default_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_default(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_1.equal
        __hash__ = _u_capture_1.hash_function
        __lt__ = _u_capture_1.less
        __le__ = _u_capture_1.less_equal
        __gt__ = _u_capture_1.greater
        __ge__ = _u_capture_1.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_default_Current(_u_capture_0_default):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_default_Working(_u_capture_0_default):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_default.__undoable_views__ = {'default': _u_capture_0_default, 'current': _u_capture_0_default_Current, 'working': _u_capture_0_default_Working}
    return _u_capture_0_default

# Generated model: _u_capture_0_working
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_working(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_working_Current(_u_capture_0_working):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_working_Working(_u_capture_0_working):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_working.__undoable_views__ = {'default': _u_capture_0_working, 'current': _u_capture_0_working_Current, 'working': _u_capture_0_working_Working}
    return _u_capture_0_working

# Generated model: _u_capture_0_working_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_working(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_1.equal
        __hash__ = _u_capture_1.hash_function
        __lt__ = _u_capture_1.less
        __le__ = _u_capture_1.less_equal
        __gt__ = _u_capture_1.greater
        __ge__ = _u_capture_1.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_working_Current(_u_capture_0_working):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_working_Working(_u_capture_0_working):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_working.__undoable_views__ = {'default': _u_capture_0_working, 'current': _u_capture_0_working_Current, 'working': _u_capture_0_working_Working}
    return _u_capture_0_working

# Generated model: _u_historical_eq
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_historical_eq(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_historical_eq_Current(_u_historical_eq):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_historical_eq_Working(_u_historical_eq):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_historical_eq.__undoable_views__ = {'default': _u_historical_eq, 'current': _u_historical_eq_Current, 'working': _u_historical_eq_Working}
    return _u_historical_eq

# Generated model: _u_historical_eq_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_historical_eq(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_historical_eq_Current(_u_historical_eq):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_historical_eq_Working(_u_historical_eq):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_historical_eq.__undoable_views__ = {'default': _u_historical_eq, 'current': _u_historical_eq_Current, 'working': _u_historical_eq_Working}
    return _u_historical_eq

# Generated model: _u_historical_hash
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_historical_hash(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_historical_hash_Current(_u_historical_hash):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_historical_hash_Working(_u_historical_hash):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_historical_hash.__undoable_views__ = {'default': _u_historical_hash, 'current': _u_historical_hash_Current, 'working': _u_historical_hash_Working}
    return _u_historical_hash

# Generated model: _u_historical_hash_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_historical_hash(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_historical_hash_Current(_u_historical_hash):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_historical_hash_Working(_u_historical_hash):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_historical_hash.__undoable_views__ = {'default': _u_historical_hash, 'current': _u_historical_hash_Current, 'working': _u_historical_hash_Working}
    return _u_historical_hash

# Generated model: _u_historical_write_scope
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_historical_write_scope(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_historical_write_scope_Current(_u_historical_write_scope):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_historical_write_scope_Working(_u_historical_write_scope):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_historical_write_scope.__undoable_views__ = {'default': _u_historical_write_scope, 'current': _u_historical_write_scope_Current, 'working': _u_historical_write_scope_Working}
    return _u_historical_write_scope

# Generated model: _u_historical_write_scope_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_historical_write_scope(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_historical_write_scope_Current(_u_historical_write_scope):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_historical_write_scope_Working(_u_historical_write_scope):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_historical_write_scope.__undoable_views__ = {'default': _u_historical_write_scope, 'current': _u_historical_write_scope_Current, 'working': _u_historical_write_scope_Working}
    return _u_historical_write_scope

# Generated model: _u_object_ge
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_ge(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_ge_Current(_u_object_ge):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_ge_Working(_u_object_ge):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_ge.__undoable_views__ = {'default': _u_object_ge, 'current': _u_object_ge_Current, 'working': _u_object_ge_Working}
    return _u_object_ge

# Generated model: _u_object_ge_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_ge(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_ge_Current(_u_object_ge):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_ge_Working(_u_object_ge):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_ge.__undoable_views__ = {'default': _u_object_ge, 'current': _u_object_ge_Current, 'working': _u_object_ge_Working}
    return _u_object_ge

# Generated model: _u_object_gt
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_gt(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_gt_Current(_u_object_gt):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_gt_Working(_u_object_gt):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_gt.__undoable_views__ = {'default': _u_object_gt, 'current': _u_object_gt_Current, 'working': _u_object_gt_Working}
    return _u_object_gt

# Generated model: _u_object_gt_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_gt(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_gt_Current(_u_object_gt):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_gt_Working(_u_object_gt):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_gt.__undoable_views__ = {'default': _u_object_gt, 'current': _u_object_gt_Current, 'working': _u_object_gt_Working}
    return _u_object_gt

# Generated model: _u_object_le
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_le(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_le_Current(_u_object_le):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_le_Working(_u_object_le):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_le.__undoable_views__ = {'default': _u_object_le, 'current': _u_object_le_Current, 'working': _u_object_le_Working}
    return _u_object_le

# Generated model: _u_object_le_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_le(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_le_Current(_u_object_le):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_le_Working(_u_object_le):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_le.__undoable_views__ = {'default': _u_object_le, 'current': _u_object_le_Current, 'working': _u_object_le_Working}
    return _u_object_le

# Generated model: _u_object_lt
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_lt(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_lt_Current(_u_object_lt):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_lt_Working(_u_object_lt):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_lt.__undoable_views__ = {'default': _u_object_lt, 'current': _u_object_lt_Current, 'working': _u_object_lt_Working}
    return _u_object_lt

# Generated model: _u_object_lt_Disabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_object_lt(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_0.equal
        __hash__ = _u_capture_0.hash_function
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_object_lt_Current(_u_object_lt):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_object_lt_Working(_u_object_lt):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_object_lt.__undoable_views__ = {'default': _u_object_lt, 'current': _u_object_lt_Current, 'working': _u_object_lt_Working}
    return _u_object_lt

# Generated model: child
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_working(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        __eq__ = _u_capture_1.equal
        __hash__ = _u_capture_1.hash_function
        __lt__ = _u_capture_1.less
        __le__ = _u_capture_1.less_equal
        __gt__ = _u_capture_1.greater
        __ge__ = _u_capture_1.greater_equal
        pass
        pass
        pass
        pass
        pass
        pass
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_working_Current(_u_capture_0_working):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_working_Working(_u_capture_0_working):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_working.__undoable_views__ = {'default': _u_capture_0_working, 'current': _u_capture_0_working_Current, 'working': _u_capture_0_working_Working}
    return _u_capture_0_working

# Generated model: model
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class _u_capture_0_working(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_default.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, ignored=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['ignored'] = ignored
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)

    class _u_capture_0_working_Current(_u_capture_0_working):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_current_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_current_managed('ignored', value)

    class _u_capture_0_working_Working(_u_capture_0_working):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_1_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_1_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) == (other.value if True else None,)

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) < (other.value if True else None,)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) <= (other.value if True else None,)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) > (other.value if True else None,)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.value if True else None,) >= (other.value if True else None,)
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def ignored(self):
            return self._u_read_working_managed('ignored')

        @ignored.setter
        def ignored(self, value):
            self._u_write_managed('ignored', value)
    _u_capture_0_working.__undoable_views__ = {'default': _u_capture_0_working, 'current': _u_capture_0_working_Current, 'working': _u_capture_0_working_Working}
    return _u_capture_0_working
