# Generated model: Forward
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Forward(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, source=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['source'] = source
            state.inputs['constant'] = constant
            state.inputs['value'] = value
            self._u_finish(state)

        @property
        def source(self):
            return self._u_read_factory_static('source')

        @source.setter
        def source(self, value):
            self._u_write_once_static('source', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class Forward_Current(Forward):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

    class Forward_Working(Forward):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)
    Forward.__undoable_views__ = {'default': Forward, 'current': Forward_Current, 'working': Forward_Working}
    return Forward

# Generated model: Reverse
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Reverse(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, source=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['constant'] = constant
            state.inputs['source'] = source
            self._u_finish(state)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def source(self):
            return self._u_read_factory_static('source')

        @source.setter
        def source(self, value):
            self._u_write_once_static('source', value)

    class Reverse_Current(Reverse):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

    class Reverse_Working(Reverse):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)
    Reverse.__undoable_views__ = {'default': Reverse, 'current': Reverse_Current, 'working': Reverse_Working}
    return Reverse
