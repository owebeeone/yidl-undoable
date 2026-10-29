# Generated model: Node
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY

def build_undoable_class(base_cls, *, schema):

    class Node(base_cls):
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

        def __init__(self, *, transaction_manager, number=_HAS_DEFAULT_FACTORY, children=_HAS_DEFAULT_FACTORY, resource=_HAS_DEFAULT_FACTORY):
            state = self._u_start(transaction_manager)
            state.inputs['number'] = number
            state.inputs['children'] = children
            state.inputs['resource'] = resource
            self._u_finish(state)
        __init__.__annotations__ = {fact['field_name']: fact['annotation'] for fact in schema.fields if fact['init'] and fact['field_kind'] not in {'classvar', 'local_store'}}

        @property
        def number(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'number' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'number' + ': unresolved constructor field')
                return state.values['number']
            return state.manager._read_managed(self, 'number')

        @number.setter
        def number(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('number' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'number', value)

        @property
        def children(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'children' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'children' + ': unresolved constructor field')
                return state.values['children']
            return state.manager._read_managed(self, 'children')

        @children.setter
        def children(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('children' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'children', value)

        @property
        def resource(self):
            state = self._u_state
            if 'resource' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'resource' + ': unresolved constructor field')
            return state.values['resource']

        @resource.setter
        def resource(self, value):
            self._u_state.values['resource'] = value

    class Node_Current(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def number(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'number' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'number' + ': unresolved constructor field')
                return state.values['number']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'number')
            return state.manager._committed_value(self, 'number')

        @number.setter
        def number(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('number' + ': current managed facade is read-only')

        @property
        def children(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'children' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'children' + ': unresolved constructor field')
                return state.values['children']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'children')
            return state.manager._committed_value(self, 'children')

        @children.setter
        def children(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('children' + ': current managed facade is read-only')

    class Node_Working(Node):
        __slots__ = ()
        pass
        pass
        pass
        pass
        pass
        pass

        @property
        def number(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'number' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'number' + ': unresolved constructor field')
                return state.values['number']
            return state.manager._read_managed(self, 'number')

        @number.setter
        def number(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('number' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'number', value)

        @property
        def children(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'children' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'children' + ': unresolved constructor field')
                return state.values['children']
            return state.manager._read_managed(self, 'children')

        @children.setter
        def children(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('children' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'children', value)
    Node.__undoable_views__ = {'default': Node, 'current': Node_Current, 'working': Node_Working}
    return Node
