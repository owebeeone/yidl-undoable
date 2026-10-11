# Generated model: Checked
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Checked(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, valid=_HAS_DEFAULT_FACTORY, attack=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['valid'] = valid
            state.inputs['attack'] = attack
            self._u_finish(state)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def items(self):
            return self._u_read_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)

        @property
        def valid(self):
            return self._u_read_plain('valid')

        @valid.setter
        def valid(self, value):
            self._u_write_plain('valid', value)

        @property
        def seen(self):
            return self._u_read_plain('seen')

        @seen.setter
        def seen(self, value):
            self._u_write_plain('seen', value)

        @property
        def attack(self):
            return self._u_read_plain('attack')

        @attack.setter
        def attack(self, value):
            self._u_write_plain('attack', value)

    class Checked_Current(Checked):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_current_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_current_managed('value', value)

        @property
        def items(self):
            return self._u_read_current_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_current_managed('items', value)

    class Checked_Working(Checked):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def items(self):
            return self._u_read_thaw_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)
    Checked.__undoable_views__ = {'default': Checked, 'current': Checked_Current, 'working': Checked_Working}
    return Checked

# Generated model: Frozen
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Frozen(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, data=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['data'] = data
            self._u_finish(state)

        @property
        def data(self):
            return self._u_read_managed('data')

        @data.setter
        def data(self, value):
            self._u_write_managed('data', value)

    class Frozen_Current(Frozen):
        __slots__ = ()

        @property
        def data(self):
            return self._u_read_current_managed('data')

        @data.setter
        def data(self, value):
            self._u_write_current_managed('data', value)

    class Frozen_Working(Frozen):
        __slots__ = ()

        @property
        def data(self):
            return self._u_read_working_managed('data')

        @data.setter
        def data(self, value):
            self._u_write_managed('data', value)
    Frozen.__undoable_views__ = {'default': Frozen, 'current': Frozen_Current, 'working': Frozen_Working}
    return Frozen

# Generated model: MappingNode
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class MappingNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, mapping=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['mapping'] = mapping
            self._u_finish(state)

        @property
        def mapping(self):
            return self._u_read_managed('mapping')

        @mapping.setter
        def mapping(self, value):
            self._u_write_managed('mapping', value)

    class MappingNode_Current(MappingNode):
        __slots__ = ()

        @property
        def mapping(self):
            return self._u_read_current_managed('mapping')

        @mapping.setter
        def mapping(self, value):
            self._u_write_current_managed('mapping', value)

    class MappingNode_Working(MappingNode):
        __slots__ = ()

        @property
        def mapping(self):
            return self._u_read_working_managed('mapping')

        @mapping.setter
        def mapping(self, value):
            self._u_write_managed('mapping', value)
    MappingNode.__undoable_views__ = {'default': MappingNode, 'current': MappingNode_Current, 'working': MappingNode_Working}
    return MappingNode
