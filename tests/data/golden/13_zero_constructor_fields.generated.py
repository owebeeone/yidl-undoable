# Generated model: ClassOnly
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ClassOnly(base_cls):
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
        label = schema.by_name['label']['default_value']

        def __init__(self, *, transaction_manager):
            state = self._u_start(transaction_manager)
            pass
            self._u_finish(state)
        pass

    class ClassOnly_Current(ClassOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class ClassOnly_Working(ClassOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    ClassOnly.__undoable_views__ = {'default': ClassOnly, 'current': ClassOnly_Current, 'working': ClassOnly_Working}
    return ClassOnly

# Generated model: Empty
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Empty(base_cls):
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

    class Empty_Current(Empty):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class Empty_Working(Empty):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    Empty.__undoable_views__ = {'default': Empty, 'current': Empty_Current, 'working': Empty_Working}
    return Empty

# Generated model: NoInputs
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class NoInputs(base_cls):
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

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class NoInputs_Current(NoInputs):
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

    class NoInputs_Working(NoInputs):
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
    NoInputs.__undoable_views__ = {'default': NoInputs, 'current': NoInputs_Current, 'working': NoInputs_Working}
    return NoInputs

# Generated model: ScratchOnly
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class ScratchOnly(base_cls):
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

        @property
        def cache(self):
            return self._u_read_plain('cache')

        @cache.setter
        def cache(self, value):
            self._u_write_plain('cache', value)

    class ScratchOnly_Current(ScratchOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass

    class ScratchOnly_Working(ScratchOnly):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    ScratchOnly.__undoable_views__ = {'default': ScratchOnly, 'current': ScratchOnly_Current, 'working': ScratchOnly_Working}
    return ScratchOnly

# Generated model: kind
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class NoInputs(base_cls):
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

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class NoInputs_Current(NoInputs):
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

    class NoInputs_Working(NoInputs):
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
    NoInputs.__undoable_views__ = {'default': NoInputs, 'current': NoInputs_Current, 'working': NoInputs_Working}
    return NoInputs
