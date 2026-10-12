# Generated model: Child
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Child(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.value == other.value

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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            self._u_finish(state)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class Child_Current(Child):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.value == other.value

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

    class Child_Working(Child):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.value == other.value

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

# Generated model: Parent_False_False_legacy_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_False_legacy_identity(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_False_legacy_identity_Current(Parent_False_False_legacy_identity):
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

    class Parent_False_False_legacy_identity_Working(Parent_False_False_legacy_identity):
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
    Parent_False_False_legacy_identity.__undoable_views__ = {'default': Parent_False_False_legacy_identity, 'current': Parent_False_False_legacy_identity_Current, 'working': Parent_False_False_legacy_identity_Working}
    return Parent_False_False_legacy_identity

# Generated model: Parent_False_False_legacy_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_False_legacy_value(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_False_legacy_value_Current(Parent_False_False_legacy_value):
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

    class Parent_False_False_legacy_value_Working(Parent_False_False_legacy_value):
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
    Parent_False_False_legacy_value.__undoable_views__ = {'default': Parent_False_False_legacy_value, 'current': Parent_False_False_legacy_value_Current, 'working': Parent_False_False_legacy_value_Working}
    return Parent_False_False_legacy_value

# Generated model: Parent_False_False_new_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_False_new_identity(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_False_new_identity_Current(Parent_False_False_new_identity):
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

    class Parent_False_False_new_identity_Working(Parent_False_False_new_identity):
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
    Parent_False_False_new_identity.__undoable_views__ = {'default': Parent_False_False_new_identity, 'current': Parent_False_False_new_identity_Current, 'working': Parent_False_False_new_identity_Working}
    return Parent_False_False_new_identity

# Generated model: Parent_False_False_new_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_False_new_value(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_False_new_value_Current(Parent_False_False_new_value):
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

    class Parent_False_False_new_value_Working(Parent_False_False_new_value):
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
    Parent_False_False_new_value.__undoable_views__ = {'default': Parent_False_False_new_value, 'current': Parent_False_False_new_value_Current, 'working': Parent_False_False_new_value_Working}
    return Parent_False_False_new_value

# Generated model: Parent_False_True_legacy_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_True_legacy_identity(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_True_legacy_identity_Current(Parent_False_True_legacy_identity):
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

    class Parent_False_True_legacy_identity_Working(Parent_False_True_legacy_identity):
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
    Parent_False_True_legacy_identity.__undoable_views__ = {'default': Parent_False_True_legacy_identity, 'current': Parent_False_True_legacy_identity_Current, 'working': Parent_False_True_legacy_identity_Working}
    return Parent_False_True_legacy_identity

# Generated model: Parent_False_True_legacy_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_True_legacy_value(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_True_legacy_value_Current(Parent_False_True_legacy_value):
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

    class Parent_False_True_legacy_value_Working(Parent_False_True_legacy_value):
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
    Parent_False_True_legacy_value.__undoable_views__ = {'default': Parent_False_True_legacy_value, 'current': Parent_False_True_legacy_value_Current, 'working': Parent_False_True_legacy_value_Working}
    return Parent_False_True_legacy_value

# Generated model: Parent_False_True_new_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_True_new_identity(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_True_new_identity_Current(Parent_False_True_new_identity):
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

    class Parent_False_True_new_identity_Working(Parent_False_True_new_identity):
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
    Parent_False_True_new_identity.__undoable_views__ = {'default': Parent_False_True_new_identity, 'current': Parent_False_True_new_identity_Current, 'working': Parent_False_True_new_identity_Working}
    return Parent_False_True_new_identity

# Generated model: Parent_False_True_new_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_False_True_new_value(base_cls):
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

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_False_True_new_value_Current(Parent_False_True_new_value):
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

    class Parent_False_True_new_value_Working(Parent_False_True_new_value):
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
    Parent_False_True_new_value.__undoable_views__ = {'default': Parent_False_True_new_value, 'current': Parent_False_True_new_value_Current, 'working': Parent_False_True_new_value_Working}
    return Parent_False_True_new_value

# Generated model: Parent_True_False_legacy_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_False_legacy_identity(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_False_legacy_identity_Current(Parent_True_False_legacy_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_False_legacy_identity_Working(Parent_True_False_legacy_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_False_legacy_identity.__undoable_views__ = {'default': Parent_True_False_legacy_identity, 'current': Parent_True_False_legacy_identity_Current, 'working': Parent_True_False_legacy_identity_Working}
    return Parent_True_False_legacy_identity

# Generated model: Parent_True_False_legacy_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_False_legacy_value(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_False_legacy_value_Current(Parent_True_False_legacy_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_False_legacy_value_Working(Parent_True_False_legacy_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_False_legacy_value.__undoable_views__ = {'default': Parent_True_False_legacy_value, 'current': Parent_True_False_legacy_value_Current, 'working': Parent_True_False_legacy_value_Working}
    return Parent_True_False_legacy_value

# Generated model: Parent_True_False_new_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_False_new_identity(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return True
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_False_new_identity_Current(Parent_True_False_new_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return True
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_False_new_identity_Working(Parent_True_False_new_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return True
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_False_new_identity.__undoable_views__ = {'default': Parent_True_False_new_identity, 'current': Parent_True_False_new_identity_Current, 'working': Parent_True_False_new_identity_Working}
    return Parent_True_False_new_identity

# Generated model: Parent_True_False_new_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_False_new_value(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return True
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_False_new_value_Current(Parent_True_False_new_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return True
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_False_new_value_Working(Parent_True_False_new_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return True
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_False_new_value.__undoable_views__ = {'default': Parent_True_False_new_value, 'current': Parent_True_False_new_value_Current, 'working': Parent_True_False_new_value_Working}
    return Parent_True_False_new_value

# Generated model: Parent_True_True_legacy_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_True_legacy_identity(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_True_legacy_identity_Current(Parent_True_True_legacy_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_True_legacy_identity_Working(Parent_True_True_legacy_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_True_legacy_identity.__undoable_views__ = {'default': Parent_True_True_legacy_identity, 'current': Parent_True_True_legacy_identity_Current, 'working': Parent_True_True_legacy_identity_Working}
    return Parent_True_True_legacy_identity

# Generated model: Parent_True_True_legacy_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_True_legacy_value(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_True_legacy_value_Current(Parent_True_True_legacy_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_True_legacy_value_Working(Parent_True_True_legacy_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_True_legacy_value.__undoable_views__ = {'default': Parent_True_True_legacy_value, 'current': Parent_True_True_legacy_value_Current, 'working': Parent_True_True_legacy_value_Working}
    return Parent_True_True_legacy_value

# Generated model: Parent_True_True_new_identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_True_new_identity(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_True_new_identity_Current(Parent_True_True_new_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_True_new_identity_Working(Parent_True_True_new_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_True_new_identity.__undoable_views__ = {'default': Parent_True_True_new_identity, 'current': Parent_True_True_new_identity_Current, 'working': Parent_True_True_new_identity_Working}
    return Parent_True_True_new_identity

# Generated model: Parent_True_True_new_value
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_True_new_value(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_True_new_value_Current(Parent_True_True_new_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_True_new_value_Working(Parent_True_True_new_value):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_True_new_value.__undoable_views__ = {'default': Parent_True_True_new_value, 'current': Parent_True_True_new_value_Current, 'working': Parent_True_True_new_value_Working}
    return Parent_True_True_new_value

# Generated model: model
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Parent_True_True_new_identity(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, children=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['children'] = children
            self._u_finish(state)

        @property
        def children(self):
            return self._u_read_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)

    class Parent_True_True_new_identity_Current(Parent_True_True_new_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_current_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_current_managed('children', value)

    class Parent_True_True_new_identity_Working(Parent_True_True_new_identity):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            return self.children == other.children
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def children(self):
            return self._u_read_working_managed('children')

        @children.setter
        def children(self, value):
            self._u_write_managed('children', value)
    Parent_True_True_new_identity.__undoable_views__ = {'default': Parent_True_True_new_identity, 'current': Parent_True_True_new_identity_Current, 'working': Parent_True_True_new_identity_Working}
    return Parent_True_True_new_identity
