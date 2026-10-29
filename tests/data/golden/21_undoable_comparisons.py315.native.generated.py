# Generated model: Child
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Child(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        __lt__ = _u_capture_0.less
        __le__ = _u_capture_0.less_equal
        __gt__ = _u_capture_0.greater
        __ge__ = _u_capture_0.greater_equal

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            _y_cmp_result = self.sku == other.sku
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.stamp == other.stamp
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.resource == other.resource
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            return self.extra == other.extra
        pass
        pass
        pass
        pass
        __hash__ = None
        shared = schema.by_name['shared']['default_value']

        def __init__(self, *, transaction_manager, seed=_HAS_DEFAULT_FACTORY, sku=_HAS_DEFAULT_FACTORY, price=_HAS_DEFAULT_FACTORY, note=_HAS_DEFAULT_FACTORY, stamp=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY, extra=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['seed'] = seed
            state.inputs['sku'] = sku
            state.inputs['price'] = price
            state.inputs['note'] = note
            state.inputs['stamp'] = stamp
            state.inputs['resource'] = resource
            state.inputs['scratch'] = scratch
            state.inputs['extra'] = extra
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def sku(self):
            state = self._u_state
            if 'sku' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'sku' + ': unresolved constructor field')
            return state.values['sku']

        @sku.setter
        def sku(self, value):
            raise AttributeError('sku' + ': const reference is read-only')

        @property
        def price(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            return state.manager._read_managed(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('price' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'price', value)

        @property
        def note(self):
            state = self._u_state
            if 'note' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'note' + ': unresolved constructor field')
            return state.values['note']

        @note.setter
        def note(self, value):
            self._u_state.values['note'] = value

        @property
        def stamp(self):
            state = self._u_state
            if 'stamp' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'stamp' + ': unresolved constructor field')
            value = state.values['stamp']
            if value is _u_capture_0.missing:
                if 'stamp' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'stamp' + ': recursive lazy provider')
                fact = state.schema.by_name['stamp']
                state.resolving.add('stamp')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('stamp')
                state.values['stamp'] = value
            return value

        @stamp.setter
        def stamp(self, value):
            state = self._u_state
            if state.values['stamp'] is not _u_capture_0.missing:
                raise AttributeError('stamp' + ': lazy reference is already initialized')
            state.values['stamp'] = value

        @property
        def resource(self):
            state = self._u_state
            if 'resource' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'resource' + ': unresolved constructor field')
            return state.values['resource']

        @resource.setter
        def resource(self, value):
            state = self._u_state
            result = None
            validator = _u_capture_0.scalar_binding
            result = state.manager._call(f'{state.schema.name}.' + 'resource' + ': binding validation', lambda: validator('resource', value))
            state.values['resource'] = result

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
                    if 'scratch' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'scratch' + ': unresolved constructor field')
                    value = state.values['scratch']
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

        @property
        def cache(self):
            state = self._u_state
            if 'cache' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'cache' + ': unresolved constructor field')
            return state.values['cache']

        @cache.setter
        def cache(self, value):
            self._u_state.values['cache'] = value

        @property
        def extra(self):
            state = self._u_state
            if 'extra' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'extra' + ': unresolved constructor field')
            return state.values['extra']

        @extra.setter
        def extra(self, value):
            self._u_state.values['extra'] = value

    class Child_Current(Child):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            _y_cmp_result = self.sku == other.sku
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.stamp == other.stamp
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.resource == other.resource
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            return self.extra == other.extra
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def price(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'price')
            return state.manager._committed_value(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('price' + ': current managed facade is read-only')

    class Child_Working(Child):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            _y_cmp_result = self.sku == other.sku
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.stamp == other.stamp
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.resource == other.resource
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            return self.extra == other.extra
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def price(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            return state.manager._read_managed(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('price' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'price', value)
    Child.__undoable_views__ = {'default': Child, 'current': Child_Current, 'working': Child_Working}
    return Child

# Generated model: EmptyDisabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class EmptyDisabled(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}
        pass

    class EmptyDisabled_Current(EmptyDisabled):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class EmptyDisabled_Working(EmptyDisabled):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    EmptyDisabled.__undoable_views__ = {'default': EmptyDisabled, 'current': EmptyDisabled_Current, 'working': EmptyDisabled_Working}
    return EmptyDisabled

# Generated model: ExplicitDisabled
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ExplicitDisabled(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}
        pass

    class ExplicitDisabled_Current(ExplicitDisabled):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class ExplicitDisabled_Working(ExplicitDisabled):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    ExplicitDisabled.__undoable_views__ = {'default': ExplicitDisabled, 'current': ExplicitDisabled_Current, 'working': ExplicitDisabled_Working}
    return ExplicitDisabled

# Generated model: Identity
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Identity(base_cls):
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

        def __init__(self, *, transaction_manager, price=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['price'] = price
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def price(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            return state.manager._read_managed(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('price' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'price', value)

    class Identity_Current(Identity):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def price(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'price')
            return state.manager._committed_value(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('price' + ': current managed facade is read-only')

    class Identity_Working(Identity):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def price(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            return state.manager._read_managed(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('price' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'price', value)
    Identity.__undoable_views__ = {'default': Identity, 'current': Identity_Current, 'working': Identity_Working}
    return Identity

# Generated model: Quote
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Quote(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        pass

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_default.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_default.equal(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            _y_cmp_result = self.sku == other.sku
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.price == other.price
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.stamp == other.stamp
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            return self.resource == other.resource

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) < (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) <= (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) > (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) >= (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)
        __hash__ = None
        shared = schema.by_name['shared']['default_value']

        def __init__(self, *, transaction_manager, seed=_HAS_DEFAULT_FACTORY, sku=_HAS_DEFAULT_FACTORY, price=_HAS_DEFAULT_FACTORY, note=_HAS_DEFAULT_FACTORY, stamp=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['seed'] = seed
            state.inputs['sku'] = sku
            state.inputs['price'] = price
            state.inputs['note'] = note
            state.inputs['stamp'] = stamp
            state.inputs['resource'] = resource
            state.inputs['scratch'] = scratch
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def sku(self):
            state = self._u_state
            if 'sku' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'sku' + ': unresolved constructor field')
            return state.values['sku']

        @sku.setter
        def sku(self, value):
            raise AttributeError('sku' + ': const reference is read-only')

        @property
        def price(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            return state.manager._read_managed(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('price' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'price', value)

        @property
        def note(self):
            state = self._u_state
            if 'note' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'note' + ': unresolved constructor field')
            return state.values['note']

        @note.setter
        def note(self, value):
            self._u_state.values['note'] = value

        @property
        def stamp(self):
            state = self._u_state
            if 'stamp' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'stamp' + ': unresolved constructor field')
            value = state.values['stamp']
            if value is _u_capture_0.missing:
                if 'stamp' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'stamp' + ': recursive lazy provider')
                fact = state.schema.by_name['stamp']
                state.resolving.add('stamp')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('stamp')
                state.values['stamp'] = value
            return value

        @stamp.setter
        def stamp(self, value):
            state = self._u_state
            if state.values['stamp'] is not _u_capture_0.missing:
                raise AttributeError('stamp' + ': lazy reference is already initialized')
            state.values['stamp'] = value

        @property
        def resource(self):
            state = self._u_state
            if 'resource' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'resource' + ': unresolved constructor field')
            return state.values['resource']

        @resource.setter
        def resource(self, value):
            state = self._u_state
            result = None
            validator = _u_capture_0.scalar_binding
            result = state.manager._call(f'{state.schema.name}.' + 'resource' + ': binding validation', lambda: validator('resource', value))
            state.values['resource'] = result

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
                    if 'scratch' not in state.values:
                        raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'scratch' + ': unresolved constructor field')
                    value = state.values['scratch']
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

        @property
        def cache(self):
            state = self._u_state
            if 'cache' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'cache' + ': unresolved constructor field')
            return state.values['cache']

        @cache.setter
        def cache(self, value):
            self._u_state.values['cache'] = value

    class Quote_Current(Quote):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_current.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_current.equal(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            _y_cmp_result = self.sku == other.sku
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.price == other.price
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.stamp == other.stamp
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            return self.resource == other.resource

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) < (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) <= (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) > (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) >= (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)
        __hash__ = None

        @property
        def price(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'price')
            return state.manager._committed_value(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('price' + ': current managed facade is read-only')

    class Quote_Working(Quote):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_capture_0_working.scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_capture_0_working.equal(self, other)
            if self is other:
                return True
            if other.__class__ is not self.__class__:
                return NotImplemented
            _y_cmp_result = self.sku == other.sku
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.price == other.price
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            _y_cmp_result = self.stamp == other.stamp
            try:
                if not _y_cmp_result:
                    return _y_cmp_result
            finally:
                del _y_cmp_result
            return self.resource == other.resource

        def __lt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) < (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __le__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) <= (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __gt__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) > (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

        def __ge__(self, other):
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) >= (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)
        __hash__ = None

        @property
        def price(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'price' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'price' + ': unresolved constructor field')
                return state.values['price']
            return state.manager._read_managed(self, 'price')

        @price.setter
        def price(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('price' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'price', value)
    Quote.__undoable_views__ = {'default': Quote, 'current': Quote_Current, 'working': Quote_Working}
    return Quote

# Generated model: model
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ExplicitDisabled(base_cls):
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

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}
        pass

    class ExplicitDisabled_Current(ExplicitDisabled):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class ExplicitDisabled_Working(ExplicitDisabled):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    ExplicitDisabled.__undoable_views__ = {'default': ExplicitDisabled, 'current': ExplicitDisabled_Current, 'working': ExplicitDisabled_Working}
    return ExplicitDisabled
