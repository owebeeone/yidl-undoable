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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)

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
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'value')
            return state.manager._committed_value(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('value' + ': current managed facade is read-only')

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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)
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
            state = self._u_state
            if 'constant' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'constant' + ': unresolved constructor field')
            return state.values['constant']

        @constant.setter
        def constant(self, value):
            raise AttributeError('constant' + ': const reference is read-only')

        @property
        def plain(self):
            state = self._u_state
            if 'plain' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'plain' + ': unresolved constructor field')
            return state.values['plain']

        @plain.setter
        def plain(self, value):
            self._u_state.values['plain'] = value

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
        def cache(self):
            state = self._u_state
            if 'cache' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'cache' + ': unresolved constructor field')
            return state.values['cache']

        @cache.setter
        def cache(self, value):
            self._u_state.values['cache'] = value

        @property
        def delayed(self):
            state = self._u_state
            if 'delayed' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'delayed' + ': unresolved constructor field')
            value = state.values['delayed']
            if value is _u_capture_0.missing:
                if 'delayed' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'delayed' + ': recursive lazy provider')
                fact = state.schema.by_name['delayed']
                state.resolving.add('delayed')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('delayed')
                state.values['delayed'] = value
            return value

        @delayed.setter
        def delayed(self, value):
            state = self._u_state
            if state.values['delayed'] is not _u_capture_0.missing:
                raise AttributeError('delayed' + ': lazy reference is already initialized')
            state.values['delayed'] = value

        @property
        def replaceable(self):
            state = self._u_state
            if 'replaceable' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'replaceable' + ': unresolved constructor field')
            value = state.values['replaceable']
            if value is _u_capture_0.missing:
                if 'replaceable' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'replaceable' + ': recursive lazy provider')
                fact = state.schema.by_name['replaceable']
                state.resolving.add('replaceable')
                try:
                    value = fact['default_value']
                finally:
                    state.resolving.remove('replaceable')
                state.values['replaceable'] = value
            return value

        @replaceable.setter
        def replaceable(self, value):
            self._u_state.values['replaceable'] = value

        @property
        def temporary(self):
            state = self._u_state
            if state.constructing:
                if 'temporary' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                return state.values['temporary']
            edit = state.manager._edit
            historical_pin = self._u_pin is not None and (not isinstance(self._u_pin, _u_capture_0.candidate_type))
            if edit is None or self._u_view == 'current' or historical_pin:
                if 'temporary' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                return state.values['temporary']
            key = (state.node_id, 'temporary')
            if key not in edit.transient:
                if 'temporary' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': recursive transient provider')
                state.resolving.add('temporary')
                try:
                    value = None
                    fact = state.schema.by_name['temporary']
                    value = self._u_factory(fact, 'working_default')
                finally:
                    state.resolving.remove('temporary')
                edit.transient[key] = value
            return edit.transient[key]

        @temporary.setter
        def temporary(self, value):
            edit = self._u_state.manager._require_edit()
            if self._u_view == 'current' or self._u_pin is not None:
                raise _u_capture_0.transaction_error('current transient facade is read-only')
            edit.transient[self.node_id, 'temporary'] = value

        @property
        def value(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)

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
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'value')
            return state.manager._committed_value(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('value' + ': current managed facade is read-only')

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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)
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
            state = self._u_state
            if 'constant' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'constant' + ': unresolved constructor field')
            return state.values['constant']

        @constant.setter
        def constant(self, value):
            raise AttributeError('constant' + ': const reference is read-only')

        @property
        def plain(self):
            state = self._u_state
            if 'plain' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'plain' + ': unresolved constructor field')
            return state.values['plain']

        @plain.setter
        def plain(self, value):
            self._u_state.values['plain'] = value

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
        def cache(self):
            state = self._u_state
            if 'cache' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'cache' + ': unresolved constructor field')
            return state.values['cache']

        @cache.setter
        def cache(self, value):
            self._u_state.values['cache'] = value

        @property
        def delayed(self):
            state = self._u_state
            if 'delayed' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'delayed' + ': unresolved constructor field')
            value = state.values['delayed']
            if value is _u_capture_0.missing:
                if 'delayed' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'delayed' + ': recursive lazy provider')
                fact = state.schema.by_name['delayed']
                state.resolving.add('delayed')
                try:
                    value = self._u_factory(fact, 'default')
                finally:
                    state.resolving.remove('delayed')
                state.values['delayed'] = value
            return value

        @delayed.setter
        def delayed(self, value):
            state = self._u_state
            if state.values['delayed'] is not _u_capture_0.missing:
                raise AttributeError('delayed' + ': lazy reference is already initialized')
            state.values['delayed'] = value

        @property
        def replaceable(self):
            state = self._u_state
            if 'replaceable' not in state.values:
                raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'replaceable' + ': unresolved constructor field')
            value = state.values['replaceable']
            if value is _u_capture_0.missing:
                if 'replaceable' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'replaceable' + ': recursive lazy provider')
                fact = state.schema.by_name['replaceable']
                state.resolving.add('replaceable')
                try:
                    value = fact['default_value']
                finally:
                    state.resolving.remove('replaceable')
                state.values['replaceable'] = value
            return value

        @replaceable.setter
        def replaceable(self, value):
            self._u_state.values['replaceable'] = value

        @property
        def temporary(self):
            state = self._u_state
            if state.constructing:
                if 'temporary' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                return state.values['temporary']
            edit = state.manager._edit
            historical_pin = self._u_pin is not None and (not isinstance(self._u_pin, _u_capture_0.candidate_type))
            if edit is None or self._u_view == 'current' or historical_pin:
                if 'temporary' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': unresolved constructor field')
                return state.values['temporary']
            key = (state.node_id, 'temporary')
            if key not in edit.transient:
                if 'temporary' in state.resolving:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'temporary' + ': recursive transient provider')
                state.resolving.add('temporary')
                try:
                    value = None
                    fact = state.schema.by_name['temporary']
                    value = self._u_factory(fact, 'working_default')
                finally:
                    state.resolving.remove('temporary')
                edit.transient[key] = value
            return edit.transient[key]

        @temporary.setter
        def temporary(self, value):
            edit = self._u_state.manager._require_edit()
            if self._u_view == 'current' or self._u_pin is not None:
                raise _u_capture_0.transaction_error('current transient facade is read-only')
            edit.transient[self.node_id, 'temporary'] = value

        @property
        def value(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)

        @property
        def extra(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'extra' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'extra' + ': unresolved constructor field')
                return state.values['extra']
            return state.manager._read_managed(self, 'extra')

        @extra.setter
        def extra(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('extra' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'extra', value)

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
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'value')
            return state.manager._committed_value(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('value' + ': current managed facade is read-only')

        @property
        def extra(self):
            state = self._u_state
            state.manager._require_confirmed()
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'extra' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'extra' + ': unresolved constructor field')
                return state.values['extra']
            if self._u_pin is not None:
                return state.manager._read_managed(self, 'extra')
            return state.manager._committed_value(self, 'extra')

        @extra.setter
        def extra(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            raise _u_capture_0.transaction_error('extra' + ': current managed facade is read-only')

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
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'value' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'value' + ': unresolved constructor field')
                return state.values['value']
            return state.manager._read_managed(self, 'value')

        @value.setter
        def value(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('value' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'value', value)

        @property
        def extra(self):
            self._u_state.manager._require_confirmed()
            state = self._u_state
            if self._u_pin is None and (state.constructing or state.manager._selection is None):
                if 'extra' not in state.values:
                    raise _u_capture_0.definition_error(f'{state.schema.name}.' + 'extra' + ': unresolved constructor field')
                return state.values['extra']
            return state.manager._read_managed(self, 'extra')

        @extra.setter
        def extra(self, value):
            _u_capture_0.mutation_guard(self._u_state.manager)
            if self._u_state.constructing:
                raise _u_capture_0.transaction_error('extra' + ': constructor baselines are read-only')
            self._u_state.manager._write_managed(self, 'extra', value)
    Sub.__undoable_views__ = {'default': Sub, 'current': Sub_Current, 'working': Sub_Working}
    return Sub
