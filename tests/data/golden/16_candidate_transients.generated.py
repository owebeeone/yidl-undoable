# Generated model: Model
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Model(base_cls):
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

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY, sourced=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['scratch'] = scratch
            state.inputs['sourced'] = sourced
            self._u_finish(state)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def scratch(self):
            return self._u_read_baseline_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

        @property
        def sourced(self):
            return self._u_read_factory_transient('sourced')

        @sourced.setter
        def sourced(self, value):
            self._u_write_transient('sourced', value)

        @property
        def seen(self):
            return self._u_read_plain('seen')

        @seen.setter
        def seen(self, value):
            self._u_write_plain('seen', value)

    class Model_Current(Model):
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

    class Model_Working(Model):
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
    Model.__undoable_views__ = {'default': Model, 'current': Model_Current, 'working': Model_Working}
    return Model
