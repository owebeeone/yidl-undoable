# Generated model: Custom
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Custom(base_cls):
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

    class Custom_Current(Custom):
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

    class Custom_Working(Custom):
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
    Custom.__undoable_views__ = {'default': Custom, 'current': Custom_Current, 'working': Custom_Working}
    return Custom

# Generated model: Fields
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Fields(base_cls):
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
        class_value = schema.by_name['class_value']['default_value']

        def __init__(self, *, transaction_manager, seed=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, plain=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, replaceable=_HAS_DEFAULT_FACTORY, temporary=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['seed'] = seed
            state.inputs['constant'] = constant
            state.inputs['plain'] = plain
            state.inputs['resource'] = resource
            state.inputs['delayed'] = delayed
            state.inputs['replaceable'] = replaceable
            state.inputs['temporary'] = temporary
            state.inputs['value'] = value
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def resource(self):
            return self._u_read_binding('resource')

        @resource.setter
        def resource(self, value):
            self._u_write_scalar_binding('resource', value)

        @property
        def cache(self):
            return self._u_read_plain('cache')

        @cache.setter
        def cache(self, value):
            self._u_write_plain('cache', value)

        @property
        def delayed(self):
            return self._u_read_factory_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

        @property
        def replaceable(self):
            return self._u_read_default_static('replaceable')

        @replaceable.setter
        def replaceable(self, value):
            self._u_write_mutable_static('replaceable', value)

        @property
        def temporary(self):
            return self._u_read_factory_transient('temporary')

        @temporary.setter
        def temporary(self, value):
            self._u_write_transient('temporary', value)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class Fields_Current(Fields):
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

    class Fields_Working(Fields):
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
    Fields.__undoable_views__ = {'default': Fields, 'current': Fields_Current, 'working': Fields_Working}
    return Fields

# Generated model: Sub
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Sub(base_cls):
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
        class_value = schema.by_name['class_value']['default_value']

        def __init__(self, *, transaction_manager, seed=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, plain=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, replaceable=_HAS_DEFAULT_FACTORY, temporary=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, extra=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['seed'] = seed
            state.inputs['constant'] = constant
            state.inputs['plain'] = plain
            state.inputs['resource'] = resource
            state.inputs['delayed'] = delayed
            state.inputs['replaceable'] = replaceable
            state.inputs['temporary'] = temporary
            state.inputs['value'] = value
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
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def resource(self):
            return self._u_read_binding('resource')

        @resource.setter
        def resource(self, value):
            self._u_write_scalar_binding('resource', value)

        @property
        def cache(self):
            return self._u_read_plain('cache')

        @cache.setter
        def cache(self, value):
            self._u_write_plain('cache', value)

        @property
        def delayed(self):
            return self._u_read_factory_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

        @property
        def replaceable(self):
            return self._u_read_default_static('replaceable')

        @replaceable.setter
        def replaceable(self, value):
            self._u_write_mutable_static('replaceable', value)

        @property
        def temporary(self):
            return self._u_read_factory_transient('temporary')

        @temporary.setter
        def temporary(self, value):
            self._u_write_transient('temporary', value)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def extra(self):
            return self._u_read_managed('extra')

        @extra.setter
        def extra(self, value):
            self._u_write_managed('extra', value)

    class Sub_Current(Sub):
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
        def extra(self):
            return self._u_read_current_managed('extra')

        @extra.setter
        def extra(self, value):
            self._u_write_current_managed('extra', value)

    class Sub_Working(Sub):
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
        def extra(self):
            return self._u_read_working_managed('extra')

        @extra.setter
        def extra(self, value):
            self._u_write_managed('extra', value)
    Sub.__undoable_views__ = {'default': Sub, 'current': Sub_Current, 'working': Sub_Working}
    return Sub
