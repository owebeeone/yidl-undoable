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
        def note(self):
            state = self._u_state
            if 'note' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'note' + ': unresolved constructor field')
            return state.values['note']

        @note.setter
        def note(self, value):
            self._u_state.values['note'] = value

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
        def label(self):
            state = self._u_state
            if 'label' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'label' + ': unresolved constructor field')
            return state.values['label']

        @label.setter
        def label(self, value):
            raise AttributeError('label' + ': const reference is read-only')

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
        def label(self):
            state = self._u_state
            if 'label' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'label' + ': unresolved constructor field')
            return state.values['label']

        @label.setter
        def label(self, value):
            raise AttributeError('label' + ': const reference is read-only')

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
    Excluded.__undoable_views__ = {'default': Excluded, 'current': Excluded_Current, 'working': Excluded_Working}
    return Excluded
