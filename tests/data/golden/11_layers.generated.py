# Generated model: base
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['scratch'] = scratch
            state.inputs['resource'] = resource
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

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
        def scratch(self):
            return self._u_read_factory_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

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

    class LayerNode_Current(LayerNode):
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

    class LayerNode_Working(LayerNode):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def items(self):
            return self._u_read_working_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: binding
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['scratch'] = scratch
            state.inputs['resource'] = resource
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

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
        def scratch(self):
            return self._u_read_factory_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

        @property
        def resource(self):
            return self._u_read_binding('resource')

        @resource.setter
        def resource(self, value):
            self._u_write_scalar_binding('resource', value)

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: const_static
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: core
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: default_factories
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            state.inputs['items'] = items
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

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

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: local_store
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['scratch'] = scratch
            state.inputs['resource'] = resource
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

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
        def scratch(self):
            return self._u_read_factory_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

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

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: managed
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

        @property
        def value(self):
            return self._u_read_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: transient
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['scratch'] = scratch
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

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
        def scratch(self):
            return self._u_read_factory_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

    class LayerNode_Current(LayerNode):
        __slots__ = ()
        pass

    class LayerNode_Working(LayerNode):
        __slots__ = ()
        pass
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode

# Generated model: views
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class LayerNode(base_cls):
        __slots__ = ()
        __undoable_schema__ = schema
        pass

        def __init__(self, *, transaction_manager, plain=_HAS_DEFAULT_FACTORY, constant=_HAS_DEFAULT_FACTORY, delayed=_HAS_DEFAULT_FACTORY, value=_HAS_DEFAULT_FACTORY, items=_HAS_DEFAULT_FACTORY, scratch=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['plain'] = plain
            state.inputs['constant'] = constant
            state.inputs['delayed'] = delayed
            state.inputs['value'] = value
            state.inputs['items'] = items
            state.inputs['scratch'] = scratch
            state.inputs['resource'] = resource
            self._u_finish(state)

        @property
        def plain(self):
            return self._u_read_plain('plain')

        @plain.setter
        def plain(self, value):
            self._u_write_plain('plain', value)

        @property
        def constant(self):
            return self._u_read_const('constant')

        @constant.setter
        def constant(self, value):
            self._u_write_const('constant', value)

        @property
        def delayed(self):
            return self._u_read_default_static('delayed')

        @delayed.setter
        def delayed(self, value):
            self._u_write_once_static('delayed', value)

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
        def scratch(self):
            return self._u_read_factory_transient('scratch')

        @scratch.setter
        def scratch(self, value):
            self._u_write_transient('scratch', value)

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

    class LayerNode_Current(LayerNode):
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

    class LayerNode_Working(LayerNode):
        __slots__ = ()

        @property
        def value(self):
            return self._u_read_working_managed('value')

        @value.setter
        def value(self, value):
            self._u_write_managed('value', value)

        @property
        def items(self):
            return self._u_read_working_managed('items')

        @items.setter
        def items(self, value):
            self._u_write_managed('items', value)
    LayerNode.__undoable_views__ = {'default': LayerNode, 'current': LayerNode_Current, 'working': LayerNode_Working}
    return LayerNode
