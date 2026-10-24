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

        def __init__(self, *, transaction_manager, required, payload=_HAS_DEFAULT_FACTORY, seed=_HAS_DEFAULT_FACTORY, label=_HAS_DEFAULT_FACTORY, count=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['required'] = required
            state.inputs['payload'] = payload
            state.inputs['seed'] = seed
            state.inputs['label'] = label
            state.inputs['count'] = count
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def required(self):
            return self._u_read_const('required')

        @required.setter
        def required(self, value):
            self._u_write_const('required', value)

        @property
        def payload(self):
            return self._u_read_const('payload')

        @payload.setter
        def payload(self, value):
            self._u_write_const('payload', value)

        @property
        def seed(self):
            raise AttributeError('seed' + ': constructor-only input')

        @seed.setter
        def seed(self, value):
            raise AttributeError('seed' + ': constructor-only input')

        @property
        def label(self):
            return self._u_read_managed('label')

        @label.setter
        def label(self, value):
            self._u_write_managed('label', value)

        @property
        def count(self):
            return self._u_read_managed('count')

        @count.setter
        def count(self, value):
            self._u_write_managed('count', value)

    class Model_Current(Model):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def label(self):
            return self._u_read_current_managed('label')

        @label.setter
        def label(self, value):
            self._u_write_current_managed('label', value)

        @property
        def count(self):
            return self._u_read_current_managed('count')

        @count.setter
        def count(self, value):
            self._u_write_current_managed('count', value)

    class Model_Working(Model):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def label(self):
            return self._u_read_working_managed('label')

        @label.setter
        def label(self, value):
            self._u_write_managed('label', value)

        @property
        def count(self):
            return self._u_read_working_managed('count')

        @count.setter
        def count(self, value):
            self._u_write_managed('count', value)
    Model.__undoable_views__ = {'default': Model, 'current': Model_Current, 'working': Model_Working}
    return Model
