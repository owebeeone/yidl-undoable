from yidl.generation.data_def_sys import AddIfAbsent, DDSContainerBuilder, NOT_PROVIDED, REQUIRED, RejectDuplicate, ReplaceExisting, RuntimeCollection, RuntimeComputedCollection, RuntimeContainerSpec, RuntimePort, RuntimePortIndex, RuntimeProperty, RuntimeRecord, RuntimeUnion
_ClassIdProperty = RuntimeProperty('ClassId', str, default=REQUIRED, storage_name='class_id')
_CurrentClassNameProperty = RuntimeProperty('CurrentClassName', str, default=REQUIRED, storage_name='current_class_name')
_WorkingClassNameProperty = RuntimeProperty('WorkingClassName', str, default=REQUIRED, storage_name='working_class_name')
_ViewProperty = RuntimeProperty('View', str, default=REQUIRED, storage_name='view')
_ClassNameProperty = RuntimeProperty('ClassName', str, default=REQUIRED, storage_name='class_name')
_FieldIdProperty = RuntimeProperty('FieldId', str, default=REQUIRED, storage_name='field_id')
_FieldNameProperty = RuntimeProperty('FieldName', str, default=REQUIRED, storage_name='field_name')
_FieldOrderProperty = RuntimeProperty('FieldOrder', int, default=REQUIRED, storage_name='field_order')
_BindingShapeProperty = RuntimeProperty('BindingShape', str, default='scalar', storage_name='binding_shape')
_FieldKindProperty = RuntimeProperty('FieldKind', str, default=REQUIRED, storage_name='field_kind')
_IsLazyProperty = RuntimeProperty('IsLazy', bool, default=False, storage_name='is_lazy')
_InitProperty = RuntimeProperty('Init', bool, default=True, storage_name='init')
_HasDefaultProperty = RuntimeProperty('HasDefault', bool, default=False, storage_name='has_default')
_HasDefaultFactoryProperty = RuntimeProperty('HasDefaultFactory', bool, default=False, storage_name='has_default_factory')
_MutableProperty = RuntimeProperty('Mutable', bool, default=False, storage_name='mutable')
_HasThawProperty = RuntimeProperty('HasThaw', bool, default=False, storage_name='has_thaw')
_HasFreezeProperty = RuntimeProperty('HasFreeze', bool, default=False, storage_name='has_freeze')
_HasWorkingDefaultFactoryProperty = RuntimeProperty('HasWorkingDefaultFactory', bool, default=False, storage_name='has_working_default_factory')
_UndoableClassSpec = RuntimeRecord('UndoableClass', (_ClassIdProperty, _ClassNameProperty, _CurrentClassNameProperty, _WorkingClassNameProperty))
_FieldViewSpec = RuntimeRecord('FieldView', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _ViewProperty, _HasThawProperty))
_PlainFieldSpec = RuntimeRecord('PlainField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_InitVarFieldSpec = RuntimeRecord('InitVarField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_ClassVarFieldSpec = RuntimeRecord('ClassVarField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_ConstFieldSpec = RuntimeRecord('ConstField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_StaticFieldSpec = RuntimeRecord('StaticField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_ManagedFieldSpec = RuntimeRecord('ManagedField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_TransientFieldSpec = RuntimeRecord('TransientField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_BindingFieldSpec = RuntimeRecord('BindingField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_LocalStoreFieldSpec = RuntimeRecord('LocalStoreField', (_FieldIdProperty, _FieldNameProperty, _FieldOrderProperty, _FieldKindProperty, _BindingShapeProperty, _IsLazyProperty, _InitProperty, _HasDefaultProperty, _HasDefaultFactoryProperty, _MutableProperty, _HasThawProperty, _HasFreezeProperty, _HasWorkingDefaultFactoryProperty))
_UndoableFieldUnion = RuntimeUnion('UndoableField', (_PlainFieldSpec, _InitVarFieldSpec, _ClassVarFieldSpec, _ConstFieldSpec, _StaticFieldSpec, _ManagedFieldSpec, _TransientFieldSpec, _BindingFieldSpec, _LocalStoreFieldSpec))

class UndoableClass:
    __slots__ = ('class_id', 'class_name', 'current_class_name', 'working_class_name')
    __dds_record_spec__ = _UndoableClassSpec
    class_id: str
    class_name: str
    current_class_name: str
    working_class_name: str

    def __init__(self, *, class_id: str, class_name: str, current_class_name: str, working_class_name: str):
        if not isinstance(class_id, str):
            raise TypeError('ClassId must be str, got ' + type(class_id).__name__)
        object.__setattr__(self, 'class_id', class_id)
        if not isinstance(class_name, str):
            raise TypeError('ClassName must be str, got ' + type(class_name).__name__)
        object.__setattr__(self, 'class_name', class_name)
        if not isinstance(current_class_name, str):
            raise TypeError('CurrentClassName must be str, got ' + type(current_class_name).__name__)
        object.__setattr__(self, 'current_class_name', current_class_name)
        if not isinstance(working_class_name, str):
            raise TypeError('WorkingClassName must be str, got ' + type(working_class_name).__name__)
        object.__setattr__(self, 'working_class_name', working_class_name)

    def __setattr__(self, name, value):
        if name in ('class_id', 'class_name', 'current_class_name', 'working_class_name'):
            raise AttributeError('UndoableClass records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('class_id=' + repr(self.class_id))
        pieces.append('class_name=' + repr(self.class_name))
        pieces.append('current_class_name=' + repr(self.current_class_name))
        pieces.append('working_class_name=' + repr(self.working_class_name))
        return 'UndoableClass' + '(' + ', '.join(pieces) + ')'
_UndoableClassSpec.bind_record_class(UndoableClass)

class FieldView:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'view', 'has_thaw')
    __dds_record_spec__ = _FieldViewSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    view: str
    has_thaw: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, view: str, has_thaw: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(view, str):
            raise TypeError('View must be str, got ' + type(view).__name__)
        object.__setattr__(self, 'view', view)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'view', 'has_thaw'):
            raise AttributeError('FieldView records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('view=' + repr(self.view))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        return 'FieldView' + '(' + ', '.join(pieces) + ')'
_FieldViewSpec.bind_record_class(FieldView)

class PlainField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _PlainFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('PlainField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'PlainField' + '(' + ', '.join(pieces) + ')'
_PlainFieldSpec.bind_record_class(PlainField)

class InitVarField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _InitVarFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('InitVarField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'InitVarField' + '(' + ', '.join(pieces) + ')'
_InitVarFieldSpec.bind_record_class(InitVarField)

class ClassVarField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _ClassVarFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('ClassVarField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'ClassVarField' + '(' + ', '.join(pieces) + ')'
_ClassVarFieldSpec.bind_record_class(ClassVarField)

class ConstField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _ConstFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('ConstField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'ConstField' + '(' + ', '.join(pieces) + ')'
_ConstFieldSpec.bind_record_class(ConstField)

class StaticField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _StaticFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('StaticField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'StaticField' + '(' + ', '.join(pieces) + ')'
_StaticFieldSpec.bind_record_class(StaticField)

class ManagedField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _ManagedFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('ManagedField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'ManagedField' + '(' + ', '.join(pieces) + ')'
_ManagedFieldSpec.bind_record_class(ManagedField)

class TransientField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _TransientFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('TransientField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'TransientField' + '(' + ', '.join(pieces) + ')'
_TransientFieldSpec.bind_record_class(TransientField)

class BindingField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _BindingFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('BindingField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'BindingField' + '(' + ', '.join(pieces) + ')'
_BindingFieldSpec.bind_record_class(BindingField)

class LocalStoreField:
    __slots__ = ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory')
    __dds_record_spec__ = _LocalStoreFieldSpec
    field_id: str
    field_name: str
    field_order: int
    field_kind: str
    binding_shape: str
    is_lazy: bool
    init: bool
    has_default: bool
    has_default_factory: bool
    mutable: bool
    has_thaw: bool
    has_freeze: bool
    has_working_default_factory: bool

    def __init__(self, *, field_id: str, field_name: str, field_order: int, field_kind: str, binding_shape: str='scalar', is_lazy: bool=False, init: bool=True, has_default: bool=False, has_default_factory: bool=False, mutable: bool=False, has_thaw: bool=False, has_freeze: bool=False, has_working_default_factory: bool=False):
        if not isinstance(field_id, str):
            raise TypeError('FieldId must be str, got ' + type(field_id).__name__)
        object.__setattr__(self, 'field_id', field_id)
        if not isinstance(field_name, str):
            raise TypeError('FieldName must be str, got ' + type(field_name).__name__)
        object.__setattr__(self, 'field_name', field_name)
        if not isinstance(field_order, int):
            raise TypeError('FieldOrder must be int, got ' + type(field_order).__name__)
        object.__setattr__(self, 'field_order', field_order)
        if not isinstance(field_kind, str):
            raise TypeError('FieldKind must be str, got ' + type(field_kind).__name__)
        object.__setattr__(self, 'field_kind', field_kind)
        if not isinstance(binding_shape, str):
            raise TypeError('BindingShape must be str, got ' + type(binding_shape).__name__)
        object.__setattr__(self, 'binding_shape', binding_shape)
        if not isinstance(is_lazy, bool):
            raise TypeError('IsLazy must be bool, got ' + type(is_lazy).__name__)
        object.__setattr__(self, 'is_lazy', is_lazy)
        if not isinstance(init, bool):
            raise TypeError('Init must be bool, got ' + type(init).__name__)
        object.__setattr__(self, 'init', init)
        if not isinstance(has_default, bool):
            raise TypeError('HasDefault must be bool, got ' + type(has_default).__name__)
        object.__setattr__(self, 'has_default', has_default)
        if not isinstance(has_default_factory, bool):
            raise TypeError('HasDefaultFactory must be bool, got ' + type(has_default_factory).__name__)
        object.__setattr__(self, 'has_default_factory', has_default_factory)
        if not isinstance(mutable, bool):
            raise TypeError('Mutable must be bool, got ' + type(mutable).__name__)
        object.__setattr__(self, 'mutable', mutable)
        if not isinstance(has_thaw, bool):
            raise TypeError('HasThaw must be bool, got ' + type(has_thaw).__name__)
        object.__setattr__(self, 'has_thaw', has_thaw)
        if not isinstance(has_freeze, bool):
            raise TypeError('HasFreeze must be bool, got ' + type(has_freeze).__name__)
        object.__setattr__(self, 'has_freeze', has_freeze)
        if not isinstance(has_working_default_factory, bool):
            raise TypeError('HasWorkingDefaultFactory must be bool, got ' + type(has_working_default_factory).__name__)
        object.__setattr__(self, 'has_working_default_factory', has_working_default_factory)

    def __setattr__(self, name, value):
        if name in ('field_id', 'field_name', 'field_order', 'field_kind', 'binding_shape', 'is_lazy', 'init', 'has_default', 'has_default_factory', 'mutable', 'has_thaw', 'has_freeze', 'has_working_default_factory'):
            raise AttributeError('LocalStoreField records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('field_id=' + repr(self.field_id))
        pieces.append('field_name=' + repr(self.field_name))
        pieces.append('field_order=' + repr(self.field_order))
        pieces.append('field_kind=' + repr(self.field_kind))
        pieces.append('binding_shape=' + repr(self.binding_shape))
        pieces.append('is_lazy=' + repr(self.is_lazy))
        pieces.append('init=' + repr(self.init))
        pieces.append('has_default=' + repr(self.has_default))
        pieces.append('has_default_factory=' + repr(self.has_default_factory))
        pieces.append('mutable=' + repr(self.mutable))
        pieces.append('has_thaw=' + repr(self.has_thaw))
        pieces.append('has_freeze=' + repr(self.has_freeze))
        pieces.append('has_working_default_factory=' + repr(self.has_working_default_factory))
        return 'LocalStoreField' + '(' + ', '.join(pieces) + ')'
_LocalStoreFieldSpec.bind_record_class(LocalStoreField)
AccessViewsCollection = RuntimeCollection('AccessViews', _FieldViewSpec, allows_multiple=True, identity=(_FieldIdProperty, _ViewProperty))
ClassesCollection = RuntimeCollection('Classes', _UndoableClassSpec, allows_multiple=True, identity=_ClassIdProperty)
FieldsCollection = RuntimeCollection('Fields', _UndoableFieldUnion, allows_multiple=True, identity=_FieldIdProperty)
PlainFieldsCollection = RuntimeComputedCollection('PlainFields', source=FieldsCollection, when=(_FieldKindProperty.eq('field'),))
InitVarsCollection = RuntimeComputedCollection('InitVars', source=FieldsCollection, when=(_FieldKindProperty.eq('initvar'),))
ClassVarsCollection = RuntimeComputedCollection('ClassVars', source=FieldsCollection, when=(_FieldKindProperty.eq('classvar'),))
ConstFieldsCollection = RuntimeComputedCollection('ConstFields', source=FieldsCollection, when=(_FieldKindProperty.eq('const'),))
StaticFieldsCollection = RuntimeComputedCollection('StaticFields', source=FieldsCollection, when=(_FieldKindProperty.eq('static'),))
ManagedFieldsCollection = RuntimeComputedCollection('ManagedFields', source=FieldsCollection, when=(_FieldKindProperty.eq('managed'),))
TransientFieldsCollection = RuntimeComputedCollection('TransientFields', source=FieldsCollection, when=(_FieldKindProperty.eq('transient'),))
BindingFieldsCollection = RuntimeComputedCollection('BindingFields', source=FieldsCollection, when=(_FieldKindProperty.eq('binding'),))
LocalStoreFieldsCollection = RuntimeComputedCollection('LocalStoreFields', source=FieldsCollection, when=(_FieldKindProperty.eq('local_store'),))
ManagedAccessViewsCollection = RuntimeComputedCollection('ManagedAccessViews', source=AccessViewsCollection, when=(_FieldKindProperty.eq('managed'),))
_RUNTIME_SPEC = RuntimeContainerSpec(collections=(AccessViewsCollection, ClassesCollection, FieldsCollection), computed_collections=(PlainFieldsCollection, InitVarsCollection, ClassVarsCollection, ConstFieldsCollection, StaticFieldsCollection, ManagedFieldsCollection, TransientFieldsCollection, BindingFieldsCollection, LocalStoreFieldsCollection, ManagedAccessViewsCollection), ports=(), port_index=None)

class _GeneratedMatcherNamespace:

    def __init__(self, container):
        pass

class _GeneratedContainerBuilder:

    def __init__(self):
        self._builder = DDSContainerBuilder(_RUNTIME_SPEC)

    def add(self, *args, **kwargs):
        self._builder.add(*args, **kwargs)
        return self

    def write(self, *args, **kwargs):
        self._builder.write(*args, **kwargs)
        return self

    def children_at(self, port_address):
        return self._builder.children_at(port_address)

    def _snapshot(self):
        container = self._builder._snapshot()
        container.matchers = _GeneratedMatcherNamespace(container)
        return container

    def record(self, *args, **kwargs):
        return self._builder.record(*args, **kwargs)

    def freeze(self):
        container = self._builder.freeze()
        container.matchers = _GeneratedMatcherNamespace(container)
        return container

    def __getattr__(self, name):
        return getattr(self._builder, name)

def new_builder():
    return _GeneratedContainerBuilder()


from types import SimpleNamespace as _YidlSimpleNamespace
from yidl.generation.assembly_plan import AndConditionSpec, AssemblyEdgeSpec, AssemblyInputSpec, AssemblySpec, BindingSpec, ComposableProductionSpec, ContributionMatcherSpec, ContributionRuleSpec, ContributionSpec, EdgeApplySpec, EqConditionSpec, InlineApplySpec, LiteralValueRef, PathSegmentSpec, PathSpec, RootSpec, TargetPathSpec, TargetSpec, TupleValueRef, ValueRef
from yidl.generation.assembly_runtime import run_assembly
from yidl.generation.matcher_values import astichi_template, from_astichi_code, from_import

ASSEMBLY_PROPERTIES = {'ClassId': _YidlSimpleNamespace(name='ClassId', storage_name='class_id'), 'CurrentClassName': _YidlSimpleNamespace(name='CurrentClassName', storage_name='current_class_name'), 'WorkingClassName': _YidlSimpleNamespace(name='WorkingClassName', storage_name='working_class_name'), 'View': _YidlSimpleNamespace(name='View', storage_name='view'), 'ClassName': _YidlSimpleNamespace(name='ClassName', storage_name='class_name'), 'FieldId': _YidlSimpleNamespace(name='FieldId', storage_name='field_id'), 'FieldName': _YidlSimpleNamespace(name='FieldName', storage_name='field_name'), 'FieldOrder': _YidlSimpleNamespace(name='FieldOrder', storage_name='field_order'), 'BindingShape': _YidlSimpleNamespace(name='BindingShape', storage_name='binding_shape'), 'FieldKind': _YidlSimpleNamespace(name='FieldKind', storage_name='field_kind'), 'IsLazy': _YidlSimpleNamespace(name='IsLazy', storage_name='is_lazy'), 'Init': _YidlSimpleNamespace(name='Init', storage_name='init'), 'HasDefault': _YidlSimpleNamespace(name='HasDefault', storage_name='has_default'), 'HasDefaultFactory': _YidlSimpleNamespace(name='HasDefaultFactory', storage_name='has_default_factory'), 'Mutable': _YidlSimpleNamespace(name='Mutable', storage_name='mutable'), 'HasThaw': _YidlSimpleNamespace(name='HasThaw', storage_name='has_thaw'), 'HasFreeze': _YidlSimpleNamespace(name='HasFreeze', storage_name='has_freeze'), 'HasWorkingDefaultFactory': _YidlSimpleNamespace(name='HasWorkingDefaultFactory', storage_name='has_working_default_factory')}
ASSEMBLY_RESOURCES = {'ModuleRoot': from_astichi_code("""\
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY
def build_undoable_class(base_cls, *, schema):
    astichi_hole(class_body)
    astichi_hole(return_statement)""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=39), 'ClassBundle': astichi_template(from_astichi_code("""\
class class_name_0__astichi_arg__(astichi_pass(base_cls, outer_bind=True)):
    __slots__ = ()
    __undoable_schema__ = astichi_pass(schema, outer_bind=True)
    with astichi_hole(class_values) as astichi_fallback:
        pass
    def __init__(self, init_params__astichi_param_hole__, *, transaction_manager):
        state = self._u_start(transaction_manager)
        with astichi_hole(init_values) as astichi_fallback:
            pass
        self._u_finish(state)
    with astichi_hole(properties) as astichi_fallback:
        pass
class current_class_0__astichi_arg__(class_name_1__astichi_arg__):
    __slots__ = ()
    with astichi_hole(current_properties) as astichi_fallback:
        pass
class working_class_0__astichi_arg__(class_name_2__astichi_arg__):
    __slots__ = ()
    with astichi_hole(working_properties) as astichi_fallback:
        pass""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=45)), 'RequiredParam': astichi_template(from_astichi_code("""\
def astichi_params(*, field_name__astichi_arg__):
    pass""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=67)), 'EmptyParams': astichi_template(from_astichi_code("""\
def astichi_params():
    pass""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=71)), 'OptionalParam': astichi_template(from_astichi_code("""\
def astichi_params(*, field_name__astichi_arg__=_HAS_DEFAULT_FACTORY):
    pass""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=75, keep_names=('_HAS_DEFAULT_FACTORY',))), 'InitValue': astichi_template(from_astichi_code('astichi_pass(state, outer_bind=True).inputs[astichi_bind_external(field_name)] = astichi_pass(field_value__astichi_arg__, outer_bind=True)', file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=79)), 'HiddenInitVar': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    raise AttributeError(astichi_bind_external(field_name) + ': constructor-only input')
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    raise AttributeError(astichi_bind_external(field_name) + ': constructor-only input')""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=82)), 'ClassValue': astichi_template(from_astichi_code('field_name__astichi_arg__ = astichi_pass(schema, outer_bind=True).by_name[astichi_bind_external(field_literal)]["default_value"]', file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=96)), 'PlainProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_plain(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_plain(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=99)), 'Result': astichi_template(from_astichi_code("""\
class_registry__astichi_arg__.__undoable_views__ = {
    'default': class_default__astichi_arg__,
    'current': class_current__astichi_arg__,
    'working': class_working__astichi_arg__,
}
return class_result__astichi_arg__""", file_name='src/yidl_undoable/yidl/undoable_core.yidl', line_number=107)), 'ConstFieldProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_const(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_const(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_const_static.yidl', line_number=11)), 'StaticUnsetProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_unset_static(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    with astichi_hole(lazy_setter) as astichi_fallback:
        self._u_write_once_static(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_const_static.yidl', line_number=29)), 'StaticDefaultProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_default_static(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    with astichi_hole(lazy_setter) as astichi_fallback:
        self._u_write_once_static(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_const_static.yidl', line_number=44)), 'StaticFactoryProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_factory_static(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    with astichi_hole(lazy_setter) as astichi_fallback:
        self._u_write_once_static(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_const_static.yidl', line_number=59)), 'MutableStaticSetter': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True)._u_write_mutable_static(astichi_bind_external(field_name), astichi_pass(value, outer_bind=True))', file_name='src/yidl_undoable/yidl/undoable_const_static.yidl', line_number=74)), 'ManagedFieldProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_managed(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_managed.yidl', line_number=10)), 'TransientBaselineProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_baseline_transient(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_transient(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_transient.yidl', line_number=10)), 'TransientFactoryProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_factory_transient(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_transient(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_transient.yidl', line_number=23)), 'ScalarBindingProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_binding(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_scalar_binding(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_binding.yidl', line_number=10)), 'MapBindingProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_binding(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_map_binding(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_binding.yidl', line_number=23)), 'LocalStoreFieldProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_plain(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_plain(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_local_store.yidl', line_number=10)), 'CurrentManagedProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_current_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_current_managed(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_views.yidl', line_number=7)), 'WorkingManagedProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_working_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_managed(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_views.yidl', line_number=20)), 'ThawManagedProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_thaw_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_managed(astichi_bind_external(field_name), value)""", file_name='src/yidl_undoable/yidl/undoable_views.yidl', line_number=33))}
ASSEMBLY_CONTRIBUTIONS = {'HiddenInitVarAccessor': ContributionSpec(name='HiddenInitVarAccessor', source_name='HiddenInitVar', source_kind='resource', build_name='HiddenInitVarAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ClassDefinition': ContributionSpec(name='ClassDefinition', source_name='ClassProduction', source_kind='production', build_name='ClassDef', index=LiteralValueRef(0), order=LiteralValueRef(0), target=TargetSpec(name='class_body', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='Root', indexes=()),))),)), bindings=()), 'ReturnClass': ContributionSpec(name='ReturnClass', source_name='Result', source_kind='resource', build_name='ReturnClass', index=LiteralValueRef(0), order=LiteralValueRef(0), target=TargetSpec(name='return_statement', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='Root', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='class_registry', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='class_default', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='class_current', value=ValueRef('CurrentClassName')), BindingSpec(kind='ident', name='class_working', value=ValueRef('WorkingClassName')), BindingSpec(kind='ident', name='class_result', value=ValueRef('ClassName')))), 'Required': ContributionSpec(name='Required', source_name='RequiredParam', source_kind='resource', build_name='InitParam', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')),)), 'EmptyConstructorParams': ContributionSpec(name='EmptyConstructorParams', source_name='EmptyParams', source_kind='resource', build_name='EmptyConstructorParams', index=LiteralValueRef(-1), order=LiteralValueRef(-1), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=()), 'Default': ContributionSpec(name='Default', source_name='OptionalParam', source_kind='resource', build_name='InitParam', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')),)), 'InitAssignment': ContributionSpec(name='InitAssignment', source_name='InitValue', source_kind='resource', build_name='InitAssignment', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_values', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_value', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'PlainAccessor': ContributionSpec(name='PlainAccessor', source_name='PlainProperty', source_kind='resource', build_name='PlainAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ClassAssignment': ContributionSpec(name='ClassAssignment', source_name='ClassValue', source_kind='resource', build_name='ClassAssignment', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='class_values', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_literal', value=ValueRef('FieldName')))), 'ConstFieldAccessor': ContributionSpec(name='ConstFieldAccessor', source_name='ConstFieldProperty', source_kind='resource', build_name='ConstFieldAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'StaticUnsetAccessor': ContributionSpec(name='StaticUnsetAccessor', source_name='StaticUnsetProperty', source_kind='resource', build_name='StaticAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'StaticDefaultAccessor': ContributionSpec(name='StaticDefaultAccessor', source_name='StaticDefaultProperty', source_kind='resource', build_name='StaticAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'StaticFactoryAccessor': ContributionSpec(name='StaticFactoryAccessor', source_name='StaticFactoryProperty', source_kind='resource', build_name='StaticAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'MutableStaticSetterContribution': ContributionSpec(name='MutableStaticSetterContribution', source_name='MutableStaticSetter', source_kind='resource', build_name='MutableStaticSetterContribution', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='lazy_setter', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()), PathSegmentSpec(kind='name', name='StaticAccessor', indexes=(ValueRef('FieldOrder'),))))),)), bindings=(BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')),)), 'ManagedFieldAccessor': ContributionSpec(name='ManagedFieldAccessor', source_name='ManagedFieldProperty', source_kind='resource', build_name='ManagedFieldAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'Factory': ContributionSpec(name='Factory', source_name='OptionalParam', source_kind='resource', build_name='InitParam', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')),)), 'TransientBaselineAccessor': ContributionSpec(name='TransientBaselineAccessor', source_name='TransientBaselineProperty', source_kind='resource', build_name='TransientBaselineAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'TransientFactoryAccessor': ContributionSpec(name='TransientFactoryAccessor', source_name='TransientFactoryProperty', source_kind='resource', build_name='TransientFactoryAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ScalarBindingAccessor': ContributionSpec(name='ScalarBindingAccessor', source_name='ScalarBindingProperty', source_kind='resource', build_name='ScalarBindingAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'MapBindingAccessor': ContributionSpec(name='MapBindingAccessor', source_name='MapBindingProperty', source_kind='resource', build_name='MapBindingAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'LocalStoreFieldAccessor': ContributionSpec(name='LocalStoreFieldAccessor', source_name='LocalStoreFieldProperty', source_kind='resource', build_name='LocalStoreFieldAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'CurrentManagedAccessor': ContributionSpec(name='CurrentManagedAccessor', source_name='CurrentManagedProperty', source_kind='resource', build_name='CurrentManagedAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='current_properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'WorkingManagedAccessor': ContributionSpec(name='WorkingManagedAccessor', source_name='WorkingManagedProperty', source_kind='resource', build_name='WorkingManagedAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='working_properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ThawManagedAccessor': ContributionSpec(name='ThawManagedAccessor', source_name='ThawManagedProperty', source_kind='resource', build_name='ThawManagedAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='working_properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName'))))}
ASSEMBLY_MATCHERS = {'HiddenInitVarAccessors': ContributionMatcherSpec(name='HiddenInitVarAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='InitVars', collection=None),), default_contribution_name='HiddenInitVarAccessor', rules=()), 'ClassDefinitions': ContributionMatcherSpec(name='ClassDefinitions', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name='ClassDefinition', rules=()), 'Results': ContributionMatcherSpec(name='Results', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name='ReturnClass', rules=()), 'Constructors': ContributionMatcherSpec(name='Constructors', inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='required', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('IsLazy'), right=LiteralValueRef(False)))), contribution_name='Required', weight=1.0), ContributionRuleSpec(name='default_value', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(True)))), contribution_name='Default', weight=1.0), ContributionRuleSpec(name='lazy_unset', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('FieldKind'), right=LiteralValueRef('static')), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(False)))), contribution_name='Default', weight=1.0), ContributionRuleSpec(name='factory', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(True)))), contribution_name='Factory', weight=1.0))), 'ConstructorBoundaries': ContributionMatcherSpec(name='ConstructorBoundaries', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name='EmptyConstructorParams', rules=()), 'InitAssignments': ContributionMatcherSpec(name='InitAssignments', inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='init', condition=EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), contribution_name='InitAssignment', weight=1.0),)), 'PlainAccessors': ContributionMatcherSpec(name='PlainAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='PlainFields', collection=None),), default_contribution_name='PlainAccessor', rules=()), 'ClassAssignments': ContributionMatcherSpec(name='ClassAssignments', inputs=(AssemblyInputSpec(name='field', collection_name='ClassVars', collection=None),), default_contribution_name='ClassAssignment', rules=()), 'ConstFieldAccessors': ContributionMatcherSpec(name='ConstFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='ConstFields', collection=None),), default_contribution_name='ConstFieldAccessor', rules=()), 'StaticFieldAccessors': ContributionMatcherSpec(name='StaticFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='factory', condition=EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(True)), contribution_name='StaticFactoryAccessor', weight=1.0), ContributionRuleSpec(name='default_value', condition=EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(True)), contribution_name='StaticDefaultAccessor', weight=1.0), ContributionRuleSpec(name='unset', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(False)))), contribution_name='StaticUnsetAccessor', weight=1.0))), 'MutableStaticSetters': ContributionMatcherSpec(name='MutableStaticSetters', inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='mutable', condition=EqConditionSpec(left=ValueRef('Mutable'), right=LiteralValueRef(True)), contribution_name='MutableStaticSetterContribution', weight=1.0),)), 'ManagedFieldAccessors': ContributionMatcherSpec(name='ManagedFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='ManagedFields', collection=None),), default_contribution_name='ManagedFieldAccessor', rules=()), 'TransientFieldAccessors': ContributionMatcherSpec(name='TransientFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='TransientFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='factory', condition=EqConditionSpec(left=ValueRef('HasWorkingDefaultFactory'), right=LiteralValueRef(True)), contribution_name='TransientFactoryAccessor', weight=1.0), ContributionRuleSpec(name='baseline', condition=EqConditionSpec(left=ValueRef('HasWorkingDefaultFactory'), right=LiteralValueRef(False)), contribution_name='TransientBaselineAccessor', weight=1.0))), 'BindingFieldAccessors': ContributionMatcherSpec(name='BindingFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='BindingFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='scalar', condition=EqConditionSpec(left=ValueRef('BindingShape'), right=LiteralValueRef('scalar')), contribution_name='ScalarBindingAccessor', weight=1.0), ContributionRuleSpec(name='map', condition=EqConditionSpec(left=ValueRef('BindingShape'), right=LiteralValueRef('map')), contribution_name='MapBindingAccessor', weight=1.0))), 'LocalStoreFieldAccessors': ContributionMatcherSpec(name='LocalStoreFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='LocalStoreFields', collection=None),), default_contribution_name='LocalStoreFieldAccessor', rules=()), 'ManagedViewAccessors': ContributionMatcherSpec(name='ManagedViewAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='ManagedAccessViews', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='current', condition=EqConditionSpec(left=ValueRef('View'), right=LiteralValueRef('current')), contribution_name='CurrentManagedAccessor', weight=1.0), ContributionRuleSpec(name='thaw', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('View'), right=LiteralValueRef('working')), EqConditionSpec(left=ValueRef('HasThaw'), right=LiteralValueRef(True)))), contribution_name='ThawManagedAccessor', weight=1.0), ContributionRuleSpec(name='working', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('View'), right=LiteralValueRef('working')), EqConditionSpec(left=ValueRef('HasThaw'), right=LiteralValueRef(False)))), contribution_name='WorkingManagedAccessor', weight=1.0)))}
ASSEMBLY_EDGES = {'ModuleProduction.classes': AssemblyEdgeSpec(name='ModuleProduction.classes', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='ClassDefinitions'), 'ModuleProduction.results': AssemblyEdgeSpec(name='ModuleProduction.results', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='Results'), 'ClassProduction.constructor_boundary': AssemblyEdgeSpec(name='ClassProduction.constructor_boundary', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='ConstructorBoundaries'), 'ClassProduction.init_params': AssemblyEdgeSpec(name='ClassProduction.init_params', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='Constructors'), 'ClassProduction.init_values': AssemblyEdgeSpec(name='ClassProduction.init_values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='InitAssignments'), 'ClassProduction.values': AssemblyEdgeSpec(name='ClassProduction.values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ClassVars', collection=None),), condition=None, matcher_name='ClassAssignments'), 'ClassProduction.hidden_initvars': AssemblyEdgeSpec(name='ClassProduction.hidden_initvars', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='InitVars', collection=None),), condition=None, matcher_name='HiddenInitVarAccessors'), 'ClassProduction.properties': AssemblyEdgeSpec(name='ClassProduction.properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='PlainFields', collection=None),), condition=None, matcher_name='PlainAccessors'), 'ClassProduction.ConstField_properties': AssemblyEdgeSpec(name='ClassProduction.ConstField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ConstFields', collection=None),), condition=None, matcher_name='ConstFieldAccessors'), 'ClassProduction.StaticField_properties': AssemblyEdgeSpec(name='ClassProduction.StaticField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='StaticFieldAccessors'), 'ClassProduction.mutable_static_setters': AssemblyEdgeSpec(name='ClassProduction.mutable_static_setters', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='MutableStaticSetters'), 'ClassProduction.ManagedField_properties': AssemblyEdgeSpec(name='ClassProduction.ManagedField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedFields', collection=None),), condition=None, matcher_name='ManagedFieldAccessors'), 'ClassProduction.TransientField_properties': AssemblyEdgeSpec(name='ClassProduction.TransientField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='TransientFields', collection=None),), condition=None, matcher_name='TransientFieldAccessors'), 'ClassProduction.BindingField_properties': AssemblyEdgeSpec(name='ClassProduction.BindingField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='BindingFields', collection=None),), condition=None, matcher_name='BindingFieldAccessors'), 'ClassProduction.LocalStoreField_properties': AssemblyEdgeSpec(name='ClassProduction.LocalStoreField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='LocalStoreFields', collection=None),), condition=None, matcher_name='LocalStoreFieldAccessors'), 'ClassProduction.managed_view_properties': AssemblyEdgeSpec(name='ClassProduction.managed_view_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedAccessViews', collection=None),), condition=None, matcher_name='ManagedViewAccessors')}
ASSEMBLY_PRODUCTIONS = {'ModuleProduction': ComposableProductionSpec(name='ModuleProduction', inputs=(), root=RootSpec(build_name='Root', resource_name='ModuleRoot', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='ModuleProduction.classes', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='ClassDefinitions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ModuleProduction.results', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='Results')))), 'ClassProduction': ComposableProductionSpec(name='ClassProduction', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), root=RootSpec(build_name='ClassDef', resource_name='ClassBundle', bindings=(BindingSpec(kind='ident', name='class_name_0', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='current_class_0', value=ValueRef('CurrentClassName')), BindingSpec(kind='ident', name='class_name_1', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='working_class_0', value=ValueRef('WorkingClassName')), BindingSpec(kind='ident', name='class_name_2', value=ValueRef('ClassName')))), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.constructor_boundary', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='ConstructorBoundaries')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.init_params', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='Constructors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.init_values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='InitAssignments')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ClassVars', collection=None),), condition=None, matcher_name='ClassAssignments')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.hidden_initvars', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='InitVars', collection=None),), condition=None, matcher_name='HiddenInitVarAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='PlainFields', collection=None),), condition=None, matcher_name='PlainAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.ConstField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ConstFields', collection=None),), condition=None, matcher_name='ConstFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.StaticField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='StaticFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.mutable_static_setters', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='MutableStaticSetters')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.ManagedField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedFields', collection=None),), condition=None, matcher_name='ManagedFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.managed_view_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedAccessViews', collection=None),), condition=None, matcher_name='ManagedViewAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.TransientField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='TransientFields', collection=None),), condition=None, matcher_name='TransientFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.BindingField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='BindingFields', collection=None),), condition=None, matcher_name='BindingFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.LocalStoreField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='LocalStoreFields', collection=None),), condition=None, matcher_name='LocalStoreFieldAccessors'))))}
ASSEMBLY_ASSEMBLIES = {'UndoableModule': AssemblySpec(name='UndoableModule', production_name='ModuleProduction')}

ASSEMBLY_CONCEPT = _YidlSimpleNamespace(
    properties=ASSEMBLY_PROPERTIES,
    resources=ASSEMBLY_RESOURCES,
    contributions=ASSEMBLY_CONTRIBUTIONS,
    contribution_matchers=ASSEMBLY_MATCHERS,
    assembly_edges=ASSEMBLY_EDGES,
    composable_productions=ASSEMBLY_PRODUCTIONS,
    assemblies=ASSEMBLY_ASSEMBLIES,
)

_YIDL_BASE_BUILD_CONTAINER = globals().get('build_container')

def build_container(builder):
    if _YIDL_BASE_BUILD_CONTAINER is not None:
        return _YIDL_BASE_BUILD_CONTAINER(builder)
    return builder.freeze()

def build_assembly(entrypoint, container, *, unroll='auto'):
    return run_assembly(ASSEMBLY_CONCEPT, entrypoint, container, unroll=unroll)

def build_UndoableModule(container, *, unroll='auto'):
    return build_assembly('UndoableModule', container, unroll=unroll)
