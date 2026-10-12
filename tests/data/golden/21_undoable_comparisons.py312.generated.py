# Generated model: Child
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Child(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass
        __lt__ = _u_object_lt
        __le__ = _u_object_le
        __gt__ = _u_object_gt
        __ge__ = _u_object_ge

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.stamp if True else None, self.resource if True else None, self.extra if True else None) == (other.sku if True else None, other.stamp if True else None, other.resource if True else None, other.extra if True else None)
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

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def sku(self):
            return self._u_read_const('sku')

        @sku.setter
        def sku(self, value):
            self._u_write_const('sku', value)

        @property
        def price(self):
            return self._u_read_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_managed('price', value)

        @property
        def note(self):
            return self._u_read_plain('note')

        @note.setter
        def note(self, value):
            self._u_write_plain('note', value)

        @property
        def stamp(self):
            return self._u_read_factory_static('stamp')

        @stamp.setter
        def stamp(self, value):
            self._u_write_once_static('stamp', value)

        @property
        def resource(self):
            return self._u_read_binding('resource')

        @resource.setter
        def resource(self, value):
            self._u_write_scalar_binding('resource', value)

        @property
        def scratch(self):
            return self._u_read_baseline_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

        @property
        def cache(self):
            return self._u_read_plain('cache')

        @cache.setter
        def cache(self, value):
            self._u_write_plain('cache', value)

        @property
        def extra(self):
            return self._u_read_plain('extra')

        @extra.setter
        def extra(self, value):
            self._u_write_plain('extra', value)

    class Child_Current(Child):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.stamp if True else None, self.resource if True else None, self.extra if True else None) == (other.sku if True else None, other.stamp if True else None, other.resource if True else None, other.extra if True else None)
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def price(self):
            return self._u_read_current_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_current_managed('price', value)

    class Child_Working(Child):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.stamp if True else None, self.resource if True else None, self.extra if True else None) == (other.sku if True else None, other.stamp if True else None, other.resource if True else None, other.extra if True else None)
        pass
        pass
        pass
        pass
        __hash__ = None

        @property
        def price(self):
            return self._u_read_working_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_managed('price', value)
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

        @property
        def price(self):
            return self._u_read_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_managed('price', value)

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
            return self._u_read_current_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_current_managed('price', value)

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
            return self._u_read_working_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_managed('price', value)
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
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) == (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

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

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def sku(self):
            return self._u_read_const('sku')

        @sku.setter
        def sku(self, value):
            self._u_write_const('sku', value)

        @property
        def price(self):
            return self._u_read_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_managed('price', value)

        @property
        def note(self):
            return self._u_read_plain('note')

        @note.setter
        def note(self, value):
            self._u_write_plain('note', value)

        @property
        def stamp(self):
            return self._u_read_factory_static('stamp')

        @stamp.setter
        def stamp(self, value):
            self._u_write_once_static('stamp', value)

        @property
        def resource(self):
            return self._u_read_binding('resource')

        @resource.setter
        def resource(self, value):
            self._u_write_scalar_binding('resource', value)

        @property
        def scratch(self):
            return self._u_read_baseline_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

        @property
        def cache(self):
            return self._u_read_plain('cache')

        @cache.setter
        def cache(self, value):
            self._u_write_plain('cache', value)

    class Quote_Current(Quote):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) == (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

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
            return self._u_read_current_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_current_managed('price', value)

    class Quote_Working(Quote):
        __slots__ = ()

        def __eq__(self, other):
            if True:
                _u_write_scope = _u_historical_write_scope.get()
                if _u_write_scope is not None and _u_write_scope.active:
                    return _u_historical_eq(self, other)
            if other.__class__ is not self.__class__:
                return NotImplemented
            return (self.sku if True else None, self.price if True else None, self.stamp if True else None, self.resource if True else None) == (other.sku if True else None, other.price if True else None, other.stamp if True else None, other.resource if True else None)

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
            return self._u_read_working_managed('price')

        @price.setter
        def price(self, value):
            self._u_write_managed('price', value)
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
