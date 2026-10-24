# Generated model: After
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class After(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class After_Current(After):
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

    class After_Working(After):
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
    After.__undoable_views__ = {'default': After, 'current': After_Current, 'working': After_Working}
    return After

# Generated model: Before
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Before(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, note=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['note'] = note
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def note(self):
            return self._u_read_plain('note')

        @note.setter
        def note(self, value):
            self._u_write_plain('note', value)

    class Before_Current(Before):
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

    class Before_Working(Before):
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
    Before.__undoable_views__ = {'default': Before, 'current': Before_Current, 'working': Before_Working}
    return Before

# Generated model: Excluded
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Excluded(base_cls):
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
            return (self.label if True else None,) == (other.label if True else None,)
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, label=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['label'] = label
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def label(self):
            return self._u_read_const('label')

        @label.setter
        def label(self, value):
            self._u_write_const('label', value)

    class Excluded_Current(Excluded):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.label if True else None,) == (other.label if True else None,)
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

    class Excluded_Working(Excluded):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.label if True else None,) == (other.label if True else None,)
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)
    Excluded.__undoable_views__ = {'default': Excluded, 'current': Excluded_Current, 'working': Excluded_Working}
    return Excluded

# Generated model: model
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Excluded(base_cls):
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
            return (self.label if True else None,) == (other.label if True else None,)
        pass
        pass
        pass
        pass
        __hash__ = None
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, label=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['label'] = label
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def label(self):
            return self._u_read_const('label')

        @label.setter
        def label(self, value):
            self._u_write_const('label', value)

    class Excluded_Current(Excluded):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.label if True else None,) == (other.label if True else None,)
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

    class Excluded_Working(Excluded):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.label if True else None,) == (other.label if True else None,)
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)
    Excluded.__undoable_views__ = {'default': Excluded, 'current': Excluded_Current, 'working': Excluded_Working}
    return Excluded
