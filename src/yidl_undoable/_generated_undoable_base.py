# Regenerated with yidl-dataclass 0.1.1
# shared/comparison.yidl sha256=2f7e6df989b0714d8764de84d8a6f6b03f39c3ad7f57dba5e55f5131b8354eef
# undoable/undoable_base.yidl sha256=5838c0c66a6640fd93f213cf580f244eee5da844ee77a8c052dae02439429448
# undoable/undoable_binding.yidl sha256=b2f5bd18875042e1e552fc5eb96c88981357d25bec2f308fff4bfe8914e73df7
# undoable/undoable_comparison.yidl sha256=e7ed5acfcb1548be26a2c87329bb5ecf0a8a520b607ad39e9a8d4fc953b2d3dd
# undoable/undoable_const_static.yidl sha256=518c0e00fdf34119a130b5520fae4b39b126d238b61eb21f7c4e1ab7f6d0d8a0
# undoable/undoable_core.yidl sha256=4ce0b42b773f89d284a698a64b1e87d2a253bd35f5e82869e61aec4167635900
# undoable/undoable_default_factories.yidl sha256=8b103140dd1de0c4d4584e9acd8a92986459d803431498ae59d0f69d2a75dbcb
# undoable/undoable_local_store.yidl sha256=494830f7b105dee583e53a6a2be0e06addccdb3bac10411d0796296e4b128764
# undoable/undoable_managed.yidl sha256=e550d63f3b405415f2159797992039893498100835dbd189b8417255ec268bc4
# undoable/undoable_transient.yidl sha256=ed0901c22fc66c8f083fa60037a5cb941c4f8e73a0dd429e26a860da654c2a0b
# undoable/undoable_views.yidl sha256=4d073e76b1bd3379ef223fe913c6f356e2628777609bfc5e522150ba41c14806
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
_RestoreIdentityProperty = RuntimeProperty('RestoreIdentity', bool, default=False, storage_name='restore_identity')
_RestoreOrderProperty = RuntimeProperty('RestoreOrder', bool, default=False, storage_name='restore_order')
_CmpClassIdProperty = RuntimeProperty('CmpClassId', str, default=REQUIRED, storage_name='cmp_class_id')
_CmpClassOrderProperty = RuntimeProperty('CmpClassOrder', int, default=0, storage_name='cmp_class_order')
_CmpEqProperty = RuntimeProperty('CmpEq', bool, default=False, storage_name='cmp_eq')
_CmpOrderProperty = RuntimeProperty('CmpOrder', bool, default=False, storage_name='cmp_order')
_CmpHashProperty = RuntimeProperty('CmpHash', bool, default=False, storage_name='cmp_hash')
_CmpHashNoneProperty = RuntimeProperty('CmpHashNone', bool, default=False, storage_name='cmp_hash_none')
_UseTupleEqualityProperty = RuntimeProperty('UseTupleEquality', bool, default=True, storage_name='use_tuple_equality')
_HasCompareOperandsProperty = RuntimeProperty('HasCompareOperands', bool, default=False, storage_name='has_compare_operands')
_HasHashOperandsProperty = RuntimeProperty('HasHashOperands', bool, default=False, storage_name='has_hash_operands')
_CmpOperandIdProperty = RuntimeProperty('CmpOperandId', str, default=REQUIRED, storage_name='cmp_operand_id')
_CmpOwnerProperty = RuntimeProperty('CmpOwner', str, default=REQUIRED, storage_name='cmp_owner')
_CmpOperandOrderProperty = RuntimeProperty('CmpOperandOrder', int, default=REQUIRED, storage_name='cmp_operand_order')
_CmpReadPathProperty = RuntimeProperty('CmpReadPath', str, default=REQUIRED, storage_name='cmp_read_path')
_CmpCompareProperty = RuntimeProperty('CmpCompare', bool, default=True, storage_name='cmp_compare')
_CmpHashIncludedProperty = RuntimeProperty('CmpHashIncluded', bool, default=True, storage_name='cmp_hash_included')
_CmpLastProperty = RuntimeProperty('CmpLast', bool, default=False, storage_name='cmp_last')
_UndoableClassSpec = RuntimeRecord('UndoableClass', (_ClassIdProperty, _ClassNameProperty, _CurrentClassNameProperty, _WorkingClassNameProperty, _RestoreIdentityProperty, _RestoreOrderProperty))
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
_ComparisonClassSpec = RuntimeRecord('ComparisonClass', (_CmpClassIdProperty, _CmpClassOrderProperty, _CmpEqProperty, _CmpOrderProperty, _CmpHashProperty, _CmpHashNoneProperty, _UseTupleEqualityProperty, _HasCompareOperandsProperty, _HasHashOperandsProperty))
_ComparisonOperandSpec = RuntimeRecord('ComparisonOperand', (_CmpOperandIdProperty, _CmpOwnerProperty, _CmpOperandOrderProperty, _CmpReadPathProperty, _CmpCompareProperty, _CmpHashIncludedProperty, _CmpLastProperty))
_UndoableFieldUnion = RuntimeUnion('UndoableField', (_PlainFieldSpec, _InitVarFieldSpec, _ClassVarFieldSpec, _ConstFieldSpec, _StaticFieldSpec, _ManagedFieldSpec, _TransientFieldSpec, _BindingFieldSpec, _LocalStoreFieldSpec))

class UndoableClass:
    __slots__ = ('class_id', 'class_name', 'current_class_name', 'working_class_name', 'restore_identity', 'restore_order')
    __dds_record_spec__ = _UndoableClassSpec
    class_id: str
    class_name: str
    current_class_name: str
    working_class_name: str
    restore_identity: bool
    restore_order: bool

    def __init__(self, *, class_id: str, class_name: str, current_class_name: str, working_class_name: str, restore_identity: bool=False, restore_order: bool=False):
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
        if not isinstance(restore_identity, bool):
            raise TypeError('RestoreIdentity must be bool, got ' + type(restore_identity).__name__)
        object.__setattr__(self, 'restore_identity', restore_identity)
        if not isinstance(restore_order, bool):
            raise TypeError('RestoreOrder must be bool, got ' + type(restore_order).__name__)
        object.__setattr__(self, 'restore_order', restore_order)

    def __setattr__(self, name, value):
        if name in ('class_id', 'class_name', 'current_class_name', 'working_class_name', 'restore_identity', 'restore_order'):
            raise AttributeError('UndoableClass records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('class_id=' + repr(self.class_id))
        pieces.append('class_name=' + repr(self.class_name))
        pieces.append('current_class_name=' + repr(self.current_class_name))
        pieces.append('working_class_name=' + repr(self.working_class_name))
        pieces.append('restore_identity=' + repr(self.restore_identity))
        pieces.append('restore_order=' + repr(self.restore_order))
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

class ComparisonClass:
    __slots__ = ('cmp_class_id', 'cmp_class_order', 'cmp_eq', 'cmp_order', 'cmp_hash', 'cmp_hash_none', 'use_tuple_equality', 'has_compare_operands', 'has_hash_operands')
    __dds_record_spec__ = _ComparisonClassSpec
    cmp_class_id: str
    cmp_class_order: int
    cmp_eq: bool
    cmp_order: bool
    cmp_hash: bool
    cmp_hash_none: bool
    use_tuple_equality: bool
    has_compare_operands: bool
    has_hash_operands: bool

    def __init__(self, *, cmp_class_id: str, cmp_class_order: int=0, cmp_eq: bool=False, cmp_order: bool=False, cmp_hash: bool=False, cmp_hash_none: bool=False, use_tuple_equality: bool=True, has_compare_operands: bool=False, has_hash_operands: bool=False):
        if not isinstance(cmp_class_id, str):
            raise TypeError('CmpClassId must be str, got ' + type(cmp_class_id).__name__)
        object.__setattr__(self, 'cmp_class_id', cmp_class_id)
        if not isinstance(cmp_class_order, int):
            raise TypeError('CmpClassOrder must be int, got ' + type(cmp_class_order).__name__)
        object.__setattr__(self, 'cmp_class_order', cmp_class_order)
        if not isinstance(cmp_eq, bool):
            raise TypeError('CmpEq must be bool, got ' + type(cmp_eq).__name__)
        object.__setattr__(self, 'cmp_eq', cmp_eq)
        if not isinstance(cmp_order, bool):
            raise TypeError('CmpOrder must be bool, got ' + type(cmp_order).__name__)
        object.__setattr__(self, 'cmp_order', cmp_order)
        if not isinstance(cmp_hash, bool):
            raise TypeError('CmpHash must be bool, got ' + type(cmp_hash).__name__)
        object.__setattr__(self, 'cmp_hash', cmp_hash)
        if not isinstance(cmp_hash_none, bool):
            raise TypeError('CmpHashNone must be bool, got ' + type(cmp_hash_none).__name__)
        object.__setattr__(self, 'cmp_hash_none', cmp_hash_none)
        if not isinstance(use_tuple_equality, bool):
            raise TypeError('UseTupleEquality must be bool, got ' + type(use_tuple_equality).__name__)
        object.__setattr__(self, 'use_tuple_equality', use_tuple_equality)
        if not isinstance(has_compare_operands, bool):
            raise TypeError('HasCompareOperands must be bool, got ' + type(has_compare_operands).__name__)
        object.__setattr__(self, 'has_compare_operands', has_compare_operands)
        if not isinstance(has_hash_operands, bool):
            raise TypeError('HasHashOperands must be bool, got ' + type(has_hash_operands).__name__)
        object.__setattr__(self, 'has_hash_operands', has_hash_operands)

    def __setattr__(self, name, value):
        if name in ('cmp_class_id', 'cmp_class_order', 'cmp_eq', 'cmp_order', 'cmp_hash', 'cmp_hash_none', 'use_tuple_equality', 'has_compare_operands', 'has_hash_operands'):
            raise AttributeError('ComparisonClass records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('cmp_class_id=' + repr(self.cmp_class_id))
        pieces.append('cmp_class_order=' + repr(self.cmp_class_order))
        pieces.append('cmp_eq=' + repr(self.cmp_eq))
        pieces.append('cmp_order=' + repr(self.cmp_order))
        pieces.append('cmp_hash=' + repr(self.cmp_hash))
        pieces.append('cmp_hash_none=' + repr(self.cmp_hash_none))
        pieces.append('use_tuple_equality=' + repr(self.use_tuple_equality))
        pieces.append('has_compare_operands=' + repr(self.has_compare_operands))
        pieces.append('has_hash_operands=' + repr(self.has_hash_operands))
        return 'ComparisonClass' + '(' + ', '.join(pieces) + ')'
_ComparisonClassSpec.bind_record_class(ComparisonClass)

class ComparisonOperand:
    __slots__ = ('cmp_operand_id', 'cmp_owner', 'cmp_operand_order', 'cmp_read_path', 'cmp_compare', 'cmp_hash_included', 'cmp_last')
    __dds_record_spec__ = _ComparisonOperandSpec
    cmp_operand_id: str
    cmp_owner: str
    cmp_operand_order: int
    cmp_read_path: str
    cmp_compare: bool
    cmp_hash_included: bool
    cmp_last: bool

    def __init__(self, *, cmp_operand_id: str, cmp_owner: str, cmp_operand_order: int, cmp_read_path: str, cmp_compare: bool=True, cmp_hash_included: bool=True, cmp_last: bool=False):
        if not isinstance(cmp_operand_id, str):
            raise TypeError('CmpOperandId must be str, got ' + type(cmp_operand_id).__name__)
        object.__setattr__(self, 'cmp_operand_id', cmp_operand_id)
        if not isinstance(cmp_owner, str):
            raise TypeError('CmpOwner must be str, got ' + type(cmp_owner).__name__)
        object.__setattr__(self, 'cmp_owner', cmp_owner)
        if not isinstance(cmp_operand_order, int):
            raise TypeError('CmpOperandOrder must be int, got ' + type(cmp_operand_order).__name__)
        object.__setattr__(self, 'cmp_operand_order', cmp_operand_order)
        if not isinstance(cmp_read_path, str):
            raise TypeError('CmpReadPath must be str, got ' + type(cmp_read_path).__name__)
        object.__setattr__(self, 'cmp_read_path', cmp_read_path)
        if not isinstance(cmp_compare, bool):
            raise TypeError('CmpCompare must be bool, got ' + type(cmp_compare).__name__)
        object.__setattr__(self, 'cmp_compare', cmp_compare)
        if not isinstance(cmp_hash_included, bool):
            raise TypeError('CmpHashIncluded must be bool, got ' + type(cmp_hash_included).__name__)
        object.__setattr__(self, 'cmp_hash_included', cmp_hash_included)
        if not isinstance(cmp_last, bool):
            raise TypeError('CmpLast must be bool, got ' + type(cmp_last).__name__)
        object.__setattr__(self, 'cmp_last', cmp_last)

    def __setattr__(self, name, value):
        if name in ('cmp_operand_id', 'cmp_owner', 'cmp_operand_order', 'cmp_read_path', 'cmp_compare', 'cmp_hash_included', 'cmp_last'):
            raise AttributeError('ComparisonOperand records are immutable')
        object.__setattr__(self, name, value)

    def __repr__(self):
        pieces = []
        pieces.append('cmp_operand_id=' + repr(self.cmp_operand_id))
        pieces.append('cmp_owner=' + repr(self.cmp_owner))
        pieces.append('cmp_operand_order=' + repr(self.cmp_operand_order))
        pieces.append('cmp_read_path=' + repr(self.cmp_read_path))
        pieces.append('cmp_compare=' + repr(self.cmp_compare))
        pieces.append('cmp_hash_included=' + repr(self.cmp_hash_included))
        pieces.append('cmp_last=' + repr(self.cmp_last))
        return 'ComparisonOperand' + '(' + ', '.join(pieces) + ')'
_ComparisonOperandSpec.bind_record_class(ComparisonOperand)
AccessViewsCollection = RuntimeCollection('AccessViews', _FieldViewSpec, allows_multiple=True, identity=(_FieldIdProperty, _ViewProperty))
ClassesCollection = RuntimeCollection('Classes', _UndoableClassSpec, allows_multiple=True, identity=_ClassIdProperty)
FieldsCollection = RuntimeCollection('Fields', _UndoableFieldUnion, allows_multiple=True, identity=_FieldIdProperty)
ComparisonClassesCollection = RuntimeCollection('ComparisonClasses', _ComparisonClassSpec, allows_multiple=True, identity=_CmpClassIdProperty)
ComparisonOperandsCollection = RuntimeCollection('ComparisonOperands', _ComparisonOperandSpec, allows_multiple=True, identity=_CmpOperandIdProperty)
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
_RUNTIME_SPEC = RuntimeContainerSpec(collections=(AccessViewsCollection, ClassesCollection, FieldsCollection, ComparisonClassesCollection, ComparisonOperandsCollection), computed_collections=(PlainFieldsCollection, InitVarsCollection, ClassVarsCollection, ConstFieldsCollection, StaticFieldsCollection, ManagedFieldsCollection, TransientFieldsCollection, BindingFieldsCollection, LocalStoreFieldsCollection, ManagedAccessViewsCollection), ports=(), port_index=None)

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

ASSEMBLY_PROPERTIES = {'ClassId': _YidlSimpleNamespace(name='ClassId', storage_name='class_id'), 'CurrentClassName': _YidlSimpleNamespace(name='CurrentClassName', storage_name='current_class_name'), 'WorkingClassName': _YidlSimpleNamespace(name='WorkingClassName', storage_name='working_class_name'), 'View': _YidlSimpleNamespace(name='View', storage_name='view'), 'ClassName': _YidlSimpleNamespace(name='ClassName', storage_name='class_name'), 'FieldId': _YidlSimpleNamespace(name='FieldId', storage_name='field_id'), 'FieldName': _YidlSimpleNamespace(name='FieldName', storage_name='field_name'), 'FieldOrder': _YidlSimpleNamespace(name='FieldOrder', storage_name='field_order'), 'BindingShape': _YidlSimpleNamespace(name='BindingShape', storage_name='binding_shape'), 'FieldKind': _YidlSimpleNamespace(name='FieldKind', storage_name='field_kind'), 'IsLazy': _YidlSimpleNamespace(name='IsLazy', storage_name='is_lazy'), 'Init': _YidlSimpleNamespace(name='Init', storage_name='init'), 'HasDefault': _YidlSimpleNamespace(name='HasDefault', storage_name='has_default'), 'HasDefaultFactory': _YidlSimpleNamespace(name='HasDefaultFactory', storage_name='has_default_factory'), 'Mutable': _YidlSimpleNamespace(name='Mutable', storage_name='mutable'), 'HasThaw': _YidlSimpleNamespace(name='HasThaw', storage_name='has_thaw'), 'HasFreeze': _YidlSimpleNamespace(name='HasFreeze', storage_name='has_freeze'), 'HasWorkingDefaultFactory': _YidlSimpleNamespace(name='HasWorkingDefaultFactory', storage_name='has_working_default_factory'), 'RestoreIdentity': _YidlSimpleNamespace(name='RestoreIdentity', storage_name='restore_identity'), 'RestoreOrder': _YidlSimpleNamespace(name='RestoreOrder', storage_name='restore_order'), 'CmpClassId': _YidlSimpleNamespace(name='CmpClassId', storage_name='cmp_class_id'), 'CmpClassOrder': _YidlSimpleNamespace(name='CmpClassOrder', storage_name='cmp_class_order'), 'CmpEq': _YidlSimpleNamespace(name='CmpEq', storage_name='cmp_eq'), 'CmpOrder': _YidlSimpleNamespace(name='CmpOrder', storage_name='cmp_order'), 'CmpHash': _YidlSimpleNamespace(name='CmpHash', storage_name='cmp_hash'), 'CmpHashNone': _YidlSimpleNamespace(name='CmpHashNone', storage_name='cmp_hash_none'), 'UseTupleEquality': _YidlSimpleNamespace(name='UseTupleEquality', storage_name='use_tuple_equality'), 'HasCompareOperands': _YidlSimpleNamespace(name='HasCompareOperands', storage_name='has_compare_operands'), 'HasHashOperands': _YidlSimpleNamespace(name='HasHashOperands', storage_name='has_hash_operands'), 'CmpOperandId': _YidlSimpleNamespace(name='CmpOperandId', storage_name='cmp_operand_id'), 'CmpOwner': _YidlSimpleNamespace(name='CmpOwner', storage_name='cmp_owner'), 'CmpOperandOrder': _YidlSimpleNamespace(name='CmpOperandOrder', storage_name='cmp_operand_order'), 'CmpReadPath': _YidlSimpleNamespace(name='CmpReadPath', storage_name='cmp_read_path'), 'CmpCompare': _YidlSimpleNamespace(name='CmpCompare', storage_name='cmp_compare'), 'CmpHashIncluded': _YidlSimpleNamespace(name='CmpHashIncluded', storage_name='cmp_hash_included'), 'CmpLast': _YidlSimpleNamespace(name='CmpLast', storage_name='cmp_last')}
ASSEMBLY_RESOURCES = {'ModuleRoot': from_astichi_code("""\
from yidl_undoable.undoable_markers import _HAS_DEFAULT_FACTORY
def build_undoable_class(base_cls, *, schema):
    astichi_hole(class_body)
    astichi_hole(return_statement)""", file_name='undoable/undoable_core.yidl', line_number=41), 'ClassBundle': astichi_template(from_astichi_code("""\
class class_name_0__astichi_arg__(astichi_pass(base_cls, outer_bind=True)):
    __slots__ = ()
    __undoable_schema__ = astichi_pass(schema, outer_bind=True)
    with astichi_hole(comparison_reset) as astichi_fallback:
        pass
    with astichi_hole(order_reset) as astichi_fallback:
        pass
    with astichi_hole(default_comparison) as astichi_fallback:
        pass
    with astichi_hole(class_values) as astichi_fallback:
        pass
    def __init__(self, init_params__astichi_param_hole__, *, transaction_manager):
        state = self._u_start(transaction_manager)
        with astichi_hole(init_values) as astichi_fallback:
            pass
        self._u_finish(state)
    __init__.__annotations__ = {
        fact["field_name"]: fact["annotation"]
        for fact in astichi_pass(schema, outer_bind=True).fields
        if fact["init"] and fact["field_kind"] not in {"classvar", "local_store"}
    }
    with astichi_hole(properties) as astichi_fallback:
        pass
class current_class_0__astichi_arg__(class_name_1__astichi_arg__):
    __slots__ = ()
    with astichi_hole(current_comparison) as astichi_fallback:
        pass
    with astichi_hole(current_properties) as astichi_fallback:
        pass
class working_class_0__astichi_arg__(class_name_2__astichi_arg__):
    __slots__ = ()
    with astichi_hole(working_comparison) as astichi_fallback:
        pass
    with astichi_hole(working_properties) as astichi_fallback:
        pass""", file_name='undoable/undoable_core.yidl', line_number=47)), 'RequiredParam': astichi_template(from_astichi_code("""\
def astichi_params(*, field_name__astichi_arg__):
    pass""", file_name='undoable/undoable_core.yidl', line_number=84)), 'EmptyParams': astichi_template(from_astichi_code("""\
def astichi_params():
    pass""", file_name='undoable/undoable_core.yidl', line_number=88)), 'OptionalParam': astichi_template(from_astichi_code("""\
def astichi_params(*, field_name__astichi_arg__=_HAS_DEFAULT_FACTORY):
    pass""", file_name='undoable/undoable_core.yidl', line_number=92, keep_names=('_HAS_DEFAULT_FACTORY',))), 'InitValue': astichi_template(from_astichi_code('astichi_pass(state, outer_bind=True).inputs[astichi_bind_external(field_name)] = astichi_pass(field_value__astichi_arg__, outer_bind=True)', file_name='undoable/undoable_core.yidl', line_number=96)), 'HiddenInitVar': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    raise AttributeError(astichi_bind_external(field_name) + ': constructor-only input')
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    raise AttributeError(astichi_bind_external(field_name) + ': constructor-only input')""", file_name='undoable/undoable_core.yidl', line_number=99)), 'ClassValue': astichi_template(from_astichi_code('field_name__astichi_arg__ = astichi_pass(schema, outer_bind=True).by_name[astichi_bind_external(field_literal)]["default_value"]', file_name='undoable/undoable_core.yidl', line_number=113)), 'PlainProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_plain(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_plain(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_core.yidl', line_number=116)), 'Result': astichi_template(from_astichi_code("""\
astichi_pass(class_registry__astichi_arg__, outer_bind=True).__undoable_views__ = {
    'default': astichi_pass(class_default__astichi_arg__, outer_bind=True),
    'current': astichi_pass(class_current__astichi_arg__, outer_bind=True),
    'working': astichi_pass(class_working__astichi_arg__, outer_bind=True),
}
return astichi_pass(class_result__astichi_arg__, outer_bind=True)""", file_name='undoable/undoable_core.yidl', line_number=124)), 'ConstFieldProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_const(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_const(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_const_static.yidl', line_number=11)), 'StaticUnsetProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_unset_static(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    with astichi_hole(lazy_setter) as astichi_fallback:
        self._u_write_once_static(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_const_static.yidl', line_number=29)), 'StaticDefaultProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_default_static(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    with astichi_hole(lazy_setter) as astichi_fallback:
        self._u_write_once_static(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_const_static.yidl', line_number=44)), 'StaticFactoryProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_factory_static(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    with astichi_hole(lazy_setter) as astichi_fallback:
        self._u_write_once_static(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_const_static.yidl', line_number=59)), 'MutableStaticSetter': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True)._u_write_mutable_static(astichi_bind_external(field_name), astichi_pass(value, outer_bind=True))', file_name='undoable/undoable_const_static.yidl', line_number=74)), 'ManagedFieldProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_managed(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_managed.yidl', line_number=10)), 'TransientBaselineProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_baseline_transient(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_transient(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_transient.yidl', line_number=10)), 'TransientFactoryProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_factory_transient(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_transient(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_transient.yidl', line_number=23)), 'ScalarBindingProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_binding(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_scalar_binding(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_binding.yidl', line_number=10)), 'MapBindingProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_binding(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_map_binding(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_binding.yidl', line_number=23)), 'LocalStoreFieldProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_plain(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_plain(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_local_store.yidl', line_number=10)), 'CurrentManagedProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_current_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_current_managed(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_views.yidl', line_number=7)), 'WorkingManagedProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_working_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_managed(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_views.yidl', line_number=20)), 'ThawManagedProperty': astichi_template(from_astichi_code("""\
@property
def getter__astichi_arg__(self):
    return self._u_read_thaw_managed(astichi_bind_external(field_name))
@setter_target__astichi_arg__.setter
def setter__astichi_arg__(self, value):
    self._u_write_managed(astichi_bind_external(field_name), value)""", file_name='undoable/undoable_views.yidl', line_number=33)), 'MethodsShell': from_astichi_code("""\
astichi_hole(eq_method)
astichi_hole(order_methods)
astichi_hole(hash_method)""", file_name='shared/comparison.yidl', line_number=46), 'ComparisonPass': astichi_template(from_astichi_code('pass', file_name='shared/comparison.yidl', line_number=50, offset=40)), 'ExactClassGuard': astichi_template(from_astichi_code("""\
if astichi_pass(other, outer_bind=True).__class__ is not astichi_pass(self, outer_bind=True).__class__:
    return NotImplemented""", file_name='shared/comparison.yidl', line_number=52)), 'SelfIdentityShortcut': astichi_template(from_astichi_code("""\
if astichi_pass(self, outer_bind=True) is astichi_pass(other, outer_bind=True):
    return True""", file_name='shared/comparison.yidl', line_number=56)), 'TupleEqShell': astichi_template(from_astichi_code("""\
def __eq__(self, other):
    astichi_hole(eq_prelude)
    astichi_hole(eq_guard)
    return (*astichi_hole(eq_left),) == (*astichi_hole(eq_right),)""", file_name='shared/comparison.yidl', line_number=60, keep_names=('self', 'other', '__eq__'))), 'ChainEqShell': astichi_template(from_astichi_code("""\
def __eq__(self, other):
    astichi_hole(eq_prelude)
    astichi_hole(identity_shortcut)
    astichi_hole(eq_guard)
    astichi_hole(eq_steps)""", file_name='shared/comparison.yidl', line_number=66, keep_names=('self', 'other', '__eq__'))), 'EmptyTupleEqShell': astichi_template(from_astichi_code("""\
def __eq__(self, other):
    astichi_hole(eq_prelude)
    astichi_hole(eq_guard)
    return True""", file_name='shared/comparison.yidl', line_number=73, keep_names=('self', 'other', '__eq__'))), 'EmptyChainEqShell': astichi_template(from_astichi_code("""\
def __eq__(self, other):
    astichi_hole(eq_prelude)
    astichi_hole(identity_shortcut)
    astichi_hole(eq_guard)
    return True""", file_name='shared/comparison.yidl', line_number=79, keep_names=('self', 'other', '__eq__'))), 'EqIntermediateStep': astichi_template(from_astichi_code("""\
_y_cmp_result = astichi_pass(self, outer_bind=True).astichi_ref(external=step_path) == astichi_pass(other, outer_bind=True).astichi_ref(external=step_path)
try:
    if not _y_cmp_result:
        return _y_cmp_result
finally:
    del _y_cmp_result""", file_name='shared/comparison.yidl', line_number=86, keep_names=('_y_cmp_result',))), 'EqFinalStep': astichi_template(from_astichi_code('return astichi_pass(self, outer_bind=True).astichi_ref(external=step_path) == astichi_pass(other, outer_bind=True).astichi_ref(external=step_path)', file_name='shared/comparison.yidl', line_number=94)), 'HashShell': astichi_template(from_astichi_code("""\
def __hash__(self):
    return hash((*astichi_hole(hash_values),))""", file_name='shared/comparison.yidl', line_number=97, keep_names=('self', '__hash__'))), 'EmptyHashShell': astichi_template(from_astichi_code("""\
def __hash__(self):
    return hash(())""", file_name='shared/comparison.yidl', line_number=101, keep_names=('self', '__hash__'))), 'HashNone': astichi_template(from_astichi_code('__hash__ = None', file_name='shared/comparison.yidl', line_number=104, offset=34)), 'EqLeftRead': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True).astichi_ref(external=eq_left_path) if True else None', file_name='shared/comparison.yidl', line_number=107)), 'EqRightRead': astichi_template(from_astichi_code('astichi_pass(other, outer_bind=True).astichi_ref(external=eq_right_path) if True else None', file_name='shared/comparison.yidl', line_number=110)), 'HashValueRead': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True).astichi_ref(external=hash_path) if True else None', file_name='shared/comparison.yidl', line_number=113)), 'LtShell': astichi_template(from_astichi_code("""\
def __lt__(self, other):
    astichi_hole(order_guard)
    return (*astichi_hole(lt_left),) < (*astichi_hole(lt_right),)""", file_name='shared/comparison.yidl', line_number=116, keep_names=('self', 'other', '__lt__'))), 'EmptyLtShell': astichi_template(from_astichi_code("""\
def __lt__(self, other):
    astichi_hole(order_guard)
    return () < ()""", file_name='shared/comparison.yidl', line_number=121, keep_names=('self', 'other', '__lt__'))), 'LtLeftRead': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True).astichi_ref(external=lt_left_path) if True else None', file_name='shared/comparison.yidl', line_number=126)), 'LtRightRead': astichi_template(from_astichi_code('astichi_pass(other, outer_bind=True).astichi_ref(external=lt_right_path) if True else None', file_name='shared/comparison.yidl', line_number=129)), 'LeShell': astichi_template(from_astichi_code("""\
def __le__(self, other):
    astichi_hole(order_guard)
    return (*astichi_hole(le_left),) <= (*astichi_hole(le_right),)""", file_name='shared/comparison.yidl', line_number=132, keep_names=('self', 'other', '__le__'))), 'EmptyLeShell': astichi_template(from_astichi_code("""\
def __le__(self, other):
    astichi_hole(order_guard)
    return () <= ()""", file_name='shared/comparison.yidl', line_number=137, keep_names=('self', 'other', '__le__'))), 'LeLeftRead': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True).astichi_ref(external=le_left_path) if True else None', file_name='shared/comparison.yidl', line_number=142)), 'LeRightRead': astichi_template(from_astichi_code('astichi_pass(other, outer_bind=True).astichi_ref(external=le_right_path) if True else None', file_name='shared/comparison.yidl', line_number=145)), 'GtShell': astichi_template(from_astichi_code("""\
def __gt__(self, other):
    astichi_hole(order_guard)
    return (*astichi_hole(gt_left),) > (*astichi_hole(gt_right),)""", file_name='shared/comparison.yidl', line_number=148, keep_names=('self', 'other', '__gt__'))), 'EmptyGtShell': astichi_template(from_astichi_code("""\
def __gt__(self, other):
    astichi_hole(order_guard)
    return () > ()""", file_name='shared/comparison.yidl', line_number=153, keep_names=('self', 'other', '__gt__'))), 'GtLeftRead': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True).astichi_ref(external=gt_left_path) if True else None', file_name='shared/comparison.yidl', line_number=158)), 'GtRightRead': astichi_template(from_astichi_code('astichi_pass(other, outer_bind=True).astichi_ref(external=gt_right_path) if True else None', file_name='shared/comparison.yidl', line_number=161)), 'GeShell': astichi_template(from_astichi_code("""\
def __ge__(self, other):
    astichi_hole(order_guard)
    return (*astichi_hole(ge_left),) >= (*astichi_hole(ge_right),)""", file_name='shared/comparison.yidl', line_number=164, keep_names=('self', 'other', '__ge__'))), 'EmptyGeShell': astichi_template(from_astichi_code("""\
def __ge__(self, other):
    astichi_hole(order_guard)
    return () >= ()""", file_name='shared/comparison.yidl', line_number=169, keep_names=('self', 'other', '__ge__'))), 'GeLeftRead': astichi_template(from_astichi_code('astichi_pass(self, outer_bind=True).astichi_ref(external=ge_left_path) if True else None', file_name='shared/comparison.yidl', line_number=174)), 'GeRightRead': astichi_template(from_astichi_code('astichi_pass(other, outer_bind=True).astichi_ref(external=ge_right_path) if True else None', file_name='shared/comparison.yidl', line_number=177)), 'ViewUnhashable': astichi_template(from_astichi_code('__hash__ = None', file_name='undoable/undoable_comparison.yidl', line_number=144, offset=40, keep_names=('__hash__',))), 'HistoricalWriteIdentityPrelude': astichi_template(from_astichi_code("""\
if True:
    _u_write_scope = astichi_ref(external=capture_path).scope.get()
    if _u_write_scope is not None and _u_write_scope.active:
        return astichi_ref(external=capture_path).equal(self, other)""", file_name='undoable/undoable_comparison.yidl', line_number=158, keep_names=('self', 'other', '_u_write_scope'))), 'ResetIdentity': astichi_template(from_astichi_code("""\
__eq__ = astichi_ref(external=capture_path).equal
__hash__ = astichi_ref(external=capture_path).hash_function""", file_name='undoable/undoable_comparison.yidl', line_number=172, keep_names=('__eq__', '__hash__'))), 'ResetOrder': astichi_template(from_astichi_code("""\
__lt__ = astichi_ref(external=capture_path).less
__le__ = astichi_ref(external=capture_path).less_equal
__gt__ = astichi_ref(external=capture_path).greater
__ge__ = astichi_ref(external=capture_path).greater_equal""", file_name='undoable/undoable_comparison.yidl', line_number=176, keep_names=('__lt__', '__le__', '__gt__', '__ge__')))}
ASSEMBLY_CONTRIBUTIONS = {'HiddenInitVarAccessor': ContributionSpec(name='HiddenInitVarAccessor', source_name='HiddenInitVar', source_kind='resource', build_name='HiddenInitVarAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ClassDefinition': ContributionSpec(name='ClassDefinition', source_name='ClassProduction', source_kind='production', build_name='ClassDef', index=LiteralValueRef(0), order=LiteralValueRef(0), target=TargetSpec(name='class_body', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='Root', indexes=()),))),)), bindings=()), 'ReturnClass': ContributionSpec(name='ReturnClass', source_name='Result', source_kind='resource', build_name='ReturnClass', index=LiteralValueRef(0), order=LiteralValueRef(0), target=TargetSpec(name='return_statement', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='Root', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='class_registry', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='class_default', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='class_current', value=ValueRef('CurrentClassName')), BindingSpec(kind='ident', name='class_working', value=ValueRef('WorkingClassName')), BindingSpec(kind='ident', name='class_result', value=ValueRef('ClassName')))), 'Required': ContributionSpec(name='Required', source_name='RequiredParam', source_kind='resource', build_name='InitParam', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')),)), 'EmptyConstructorParams': ContributionSpec(name='EmptyConstructorParams', source_name='EmptyParams', source_kind='resource', build_name='EmptyConstructorParams', index=LiteralValueRef(-1), order=LiteralValueRef(-1), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=()), 'Default': ContributionSpec(name='Default', source_name='OptionalParam', source_kind='resource', build_name='InitParam', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')),)), 'InitAssignment': ContributionSpec(name='InitAssignment', source_name='InitValue', source_kind='resource', build_name='InitAssignment', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_values', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_value', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'PlainAccessor': ContributionSpec(name='PlainAccessor', source_name='PlainProperty', source_kind='resource', build_name='PlainAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ClassAssignment': ContributionSpec(name='ClassAssignment', source_name='ClassValue', source_kind='resource', build_name='ClassAssignment', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='class_values', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_literal', value=ValueRef('FieldName')))), 'ConstFieldAccessor': ContributionSpec(name='ConstFieldAccessor', source_name='ConstFieldProperty', source_kind='resource', build_name='ConstFieldAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'StaticUnsetAccessor': ContributionSpec(name='StaticUnsetAccessor', source_name='StaticUnsetProperty', source_kind='resource', build_name='StaticAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'StaticDefaultAccessor': ContributionSpec(name='StaticDefaultAccessor', source_name='StaticDefaultProperty', source_kind='resource', build_name='StaticAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'StaticFactoryAccessor': ContributionSpec(name='StaticFactoryAccessor', source_name='StaticFactoryProperty', source_kind='resource', build_name='StaticAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'MutableStaticSetterContribution': ContributionSpec(name='MutableStaticSetterContribution', source_name='MutableStaticSetter', source_kind='resource', build_name='MutableStaticSetterContribution', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='lazy_setter', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()), PathSegmentSpec(kind='name', name='StaticAccessor', indexes=(ValueRef('FieldOrder'),))))),)), bindings=(BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')),)), 'ManagedFieldAccessor': ContributionSpec(name='ManagedFieldAccessor', source_name='ManagedFieldProperty', source_kind='resource', build_name='ManagedFieldAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'Factory': ContributionSpec(name='Factory', source_name='OptionalParam', source_kind='resource', build_name='InitParam', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='init_params', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='field_name', value=ValueRef('FieldName')),)), 'TransientBaselineAccessor': ContributionSpec(name='TransientBaselineAccessor', source_name='TransientBaselineProperty', source_kind='resource', build_name='TransientBaselineAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'TransientFactoryAccessor': ContributionSpec(name='TransientFactoryAccessor', source_name='TransientFactoryProperty', source_kind='resource', build_name='TransientFactoryAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ScalarBindingAccessor': ContributionSpec(name='ScalarBindingAccessor', source_name='ScalarBindingProperty', source_kind='resource', build_name='ScalarBindingAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'MapBindingAccessor': ContributionSpec(name='MapBindingAccessor', source_name='MapBindingProperty', source_kind='resource', build_name='MapBindingAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'LocalStoreFieldAccessor': ContributionSpec(name='LocalStoreFieldAccessor', source_name='LocalStoreFieldProperty', source_kind='resource', build_name='LocalStoreFieldAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'CurrentManagedAccessor': ContributionSpec(name='CurrentManagedAccessor', source_name='CurrentManagedProperty', source_kind='resource', build_name='CurrentManagedAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='current_properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'WorkingManagedAccessor': ContributionSpec(name='WorkingManagedAccessor', source_name='WorkingManagedProperty', source_kind='resource', build_name='WorkingManagedAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='working_properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'ThawManagedAccessor': ContributionSpec(name='ThawManagedAccessor', source_name='ThawManagedProperty', source_kind='resource', build_name='ThawManagedAccessor', index=ValueRef('FieldOrder'), order=ValueRef('FieldOrder'), target=TargetSpec(name='working_properties', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='ident', name='getter', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter_target', value=ValueRef('FieldName')), BindingSpec(kind='ident', name='setter', value=ValueRef('FieldName')), BindingSpec(kind='external', name='field_name', value=ValueRef('FieldName')))), 'EmptyEq': ContributionSpec(name='EmptyEq', source_name='ComparisonPass', source_kind='resource', build_name='EmptyEq', index=None, order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'NoLt': ContributionSpec(name='NoLt', source_name='ComparisonPass', source_kind='resource', build_name='NoLt', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'NoLe': ContributionSpec(name='NoLe', source_name='ComparisonPass', source_kind='resource', build_name='NoLe', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'NoGt': ContributionSpec(name='NoGt', source_name='ComparisonPass', source_kind='resource', build_name='NoGt', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'NoGe': ContributionSpec(name='NoGe', source_name='ComparisonPass', source_kind='resource', build_name='NoGe', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyHash': ContributionSpec(name='EmptyHash', source_name='ComparisonPass', source_kind='resource', build_name='EmptyHash', index=None, order=None, target=TargetSpec(name='hash_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'NoEqPrelude': ContributionSpec(name='NoEqPrelude', source_name='ComparisonPass', source_kind='resource', build_name='NoEqPrelude', index=None, order=None, target=TargetSpec(name='eq_prelude', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=()), 'EqGuard': ContributionSpec(name='EqGuard', source_name='ExactClassGuard', source_kind='resource', build_name='EqGuard', index=None, order=None, target=TargetSpec(name='eq_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=()), 'EqIdentity': ContributionSpec(name='EqIdentity', source_name='SelfIdentityShortcut', source_kind='resource', build_name='EqIdentity', index=None, order=None, target=TargetSpec(name='identity_shortcut', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=()), 'TupleEqMethod': ContributionSpec(name='TupleEqMethod', source_name='TupleEqProduction', source_kind='production', build_name='EqMethod', index=None, order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'ChainEqMethod': ContributionSpec(name='ChainEqMethod', source_name='ChainEqProduction', source_kind='production', build_name='EqMethod', index=None, order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyTupleEqMethod': ContributionSpec(name='EmptyTupleEqMethod', source_name='EmptyTupleEqProduction', source_kind='production', build_name='EqMethod', index=None, order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyChainEqMethod': ContributionSpec(name='EmptyChainEqMethod', source_name='EmptyChainEqProduction', source_kind='production', build_name='EqMethod', index=None, order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EqLeftValue': ContributionSpec(name='EqLeftValue', source_name='EqLeftRead', source_kind='resource', build_name='EqLeftValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='eq_left', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='eq_left_path', value=ValueRef('CmpReadPath')),)), 'EqRightValue': ContributionSpec(name='EqRightValue', source_name='EqRightRead', source_kind='resource', build_name='EqRightValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='eq_right', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='eq_right_path', value=ValueRef('CmpReadPath')),)), 'HashValueValue': ContributionSpec(name='HashValueValue', source_name='HashValueRead', source_kind='resource', build_name='HashValueValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='hash_values', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='HashMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='hash_path', value=ValueRef('CmpReadPath')),)), 'IntermediateEqStep': ContributionSpec(name='IntermediateEqStep', source_name='EqIntermediateStep', source_kind='resource', build_name='EqStep', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='eq_steps', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='step_path', value=ValueRef('CmpReadPath')),)), 'FinalEqStep': ContributionSpec(name='FinalEqStep', source_name='EqFinalStep', source_kind='resource', build_name='EqStep', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='eq_steps', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='step_path', value=ValueRef('CmpReadPath')),)), 'LtMethod': ContributionSpec(name='LtMethod', source_name='LtProduction', source_kind='production', build_name='LtMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyLtMethod': ContributionSpec(name='EmptyLtMethod', source_name='EmptyLtProduction', source_kind='production', build_name='LtMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'LtGuard': ContributionSpec(name='LtGuard', source_name='ExactClassGuard', source_kind='resource', build_name='LtGuard', index=None, order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LtMethod', indexes=()),))),)), bindings=()), 'LtLeftValue': ContributionSpec(name='LtLeftValue', source_name='LtLeftRead', source_kind='resource', build_name='LtLeftValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='lt_left', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LtMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='lt_left_path', value=ValueRef('CmpReadPath')),)), 'LtRightValue': ContributionSpec(name='LtRightValue', source_name='LtRightRead', source_kind='resource', build_name='LtRightValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='lt_right', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LtMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='lt_right_path', value=ValueRef('CmpReadPath')),)), 'LeMethod': ContributionSpec(name='LeMethod', source_name='LeProduction', source_kind='production', build_name='LeMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyLeMethod': ContributionSpec(name='EmptyLeMethod', source_name='EmptyLeProduction', source_kind='production', build_name='LeMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'LeGuard': ContributionSpec(name='LeGuard', source_name='ExactClassGuard', source_kind='resource', build_name='LeGuard', index=None, order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LeMethod', indexes=()),))),)), bindings=()), 'LeLeftValue': ContributionSpec(name='LeLeftValue', source_name='LeLeftRead', source_kind='resource', build_name='LeLeftValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='le_left', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LeMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='le_left_path', value=ValueRef('CmpReadPath')),)), 'LeRightValue': ContributionSpec(name='LeRightValue', source_name='LeRightRead', source_kind='resource', build_name='LeRightValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='le_right', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LeMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='le_right_path', value=ValueRef('CmpReadPath')),)), 'GtMethod': ContributionSpec(name='GtMethod', source_name='GtProduction', source_kind='production', build_name='GtMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyGtMethod': ContributionSpec(name='EmptyGtMethod', source_name='EmptyGtProduction', source_kind='production', build_name='GtMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'GtGuard': ContributionSpec(name='GtGuard', source_name='ExactClassGuard', source_kind='resource', build_name='GtGuard', index=None, order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GtMethod', indexes=()),))),)), bindings=()), 'GtLeftValue': ContributionSpec(name='GtLeftValue', source_name='GtLeftRead', source_kind='resource', build_name='GtLeftValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='gt_left', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GtMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='gt_left_path', value=ValueRef('CmpReadPath')),)), 'GtRightValue': ContributionSpec(name='GtRightValue', source_name='GtRightRead', source_kind='resource', build_name='GtRightValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='gt_right', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GtMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='gt_right_path', value=ValueRef('CmpReadPath')),)), 'GeMethod': ContributionSpec(name='GeMethod', source_name='GeProduction', source_kind='production', build_name='GeMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyGeMethod': ContributionSpec(name='EmptyGeMethod', source_name='EmptyGeProduction', source_kind='production', build_name='GeMethod', index=None, order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'GeGuard': ContributionSpec(name='GeGuard', source_name='ExactClassGuard', source_kind='resource', build_name='GeGuard', index=None, order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GeMethod', indexes=()),))),)), bindings=()), 'GeLeftValue': ContributionSpec(name='GeLeftValue', source_name='GeLeftRead', source_kind='resource', build_name='GeLeftValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='ge_left', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GeMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='ge_left_path', value=ValueRef('CmpReadPath')),)), 'GeRightValue': ContributionSpec(name='GeRightValue', source_name='GeRightRead', source_kind='resource', build_name='GeRightValue', index=ValueRef('CmpOperandOrder'), order=ValueRef('CmpOperandOrder'), target=TargetSpec(name='ge_right', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GeMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='ge_right_path', value=ValueRef('CmpReadPath')),)), 'HashMethod': ContributionSpec(name='HashMethod', source_name='HashProduction', source_kind='production', build_name='HashMethod', index=None, order=None, target=TargetSpec(name='hash_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'EmptyHashMethod': ContributionSpec(name='EmptyHashMethod', source_name='EmptyHashProduction', source_kind='production', build_name='HashMethod', index=None, order=None, target=TargetSpec(name='hash_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'SetHashNone': ContributionSpec(name='SetHashNone', source_name='HashNone', source_kind='resource', build_name='SetHashNone', index=None, order=None, target=TargetSpec(name='hash_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedTupleEq': ContributionSpec(name='IndexedTupleEq', source_name='TupleEqProduction', source_kind='production', build_name='EqMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedChainEq': ContributionSpec(name='IndexedChainEq', source_name='ChainEqProduction', source_kind='production', build_name='EqMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyTupleEq': ContributionSpec(name='IndexedEmptyTupleEq', source_name='EmptyTupleEqProduction', source_kind='production', build_name='EqMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyChainEq': ContributionSpec(name='IndexedEmptyChainEq', source_name='EmptyChainEqProduction', source_kind='production', build_name='EqMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyEq': ContributionSpec(name='IndexedEmptyEq', source_name='ComparisonPass', source_kind='resource', build_name='EmptyEq', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEqGuard': ContributionSpec(name='IndexedEqGuard', source_name='ExactClassGuard', source_kind='resource', build_name='EqGuard', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=()), 'IndexedEqIdentity': ContributionSpec(name='IndexedEqIdentity', source_name='SelfIdentityShortcut', source_kind='resource', build_name='EqIdentity', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='identity_shortcut', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=()), 'IndexedLt': ContributionSpec(name='IndexedLt', source_name='LtProduction', source_kind='production', build_name='LtMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyLt': ContributionSpec(name='IndexedEmptyLt', source_name='EmptyLtProduction', source_kind='production', build_name='LtMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedNoLt': ContributionSpec(name='IndexedNoLt', source_name='ComparisonPass', source_kind='resource', build_name='NoLt', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedLtGuard': ContributionSpec(name='IndexedLtGuard', source_name='ExactClassGuard', source_kind='resource', build_name='LtGuard', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LtMethod', indexes=()),))),)), bindings=()), 'IndexedLe': ContributionSpec(name='IndexedLe', source_name='LeProduction', source_kind='production', build_name='LeMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyLe': ContributionSpec(name='IndexedEmptyLe', source_name='EmptyLeProduction', source_kind='production', build_name='LeMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedNoLe': ContributionSpec(name='IndexedNoLe', source_name='ComparisonPass', source_kind='resource', build_name='NoLe', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedLeGuard': ContributionSpec(name='IndexedLeGuard', source_name='ExactClassGuard', source_kind='resource', build_name='LeGuard', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='LeMethod', indexes=()),))),)), bindings=()), 'IndexedGt': ContributionSpec(name='IndexedGt', source_name='GtProduction', source_kind='production', build_name='GtMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyGt': ContributionSpec(name='IndexedEmptyGt', source_name='EmptyGtProduction', source_kind='production', build_name='GtMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedNoGt': ContributionSpec(name='IndexedNoGt', source_name='ComparisonPass', source_kind='resource', build_name='NoGt', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedGtGuard': ContributionSpec(name='IndexedGtGuard', source_name='ExactClassGuard', source_kind='resource', build_name='GtGuard', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GtMethod', indexes=()),))),)), bindings=()), 'IndexedGe': ContributionSpec(name='IndexedGe', source_name='GeProduction', source_kind='production', build_name='GeMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyGe': ContributionSpec(name='IndexedEmptyGe', source_name='EmptyGeProduction', source_kind='production', build_name='GeMethod', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedNoGe': ContributionSpec(name='IndexedNoGe', source_name='ComparisonPass', source_kind='resource', build_name='NoGe', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_methods', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedGeGuard': ContributionSpec(name='IndexedGeGuard', source_name='ExactClassGuard', source_kind='resource', build_name='GeGuard', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='order_guard', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='GeMethod', indexes=()),))),)), bindings=()), 'IndexedHashNone': ContributionSpec(name='IndexedHashNone', source_name='ViewUnhashable', source_kind='resource', build_name='SetHashNone', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='hash_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'IndexedEmptyHash': ContributionSpec(name='IndexedEmptyHash', source_name='ComparisonPass', source_kind='resource', build_name='EmptyHash', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='hash_method', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ComparisonMethods', indexes=()),))),)), bindings=()), 'HistoricalWriteIdentity': ContributionSpec(name='HistoricalWriteIdentity', source_name='HistoricalWriteIdentityPrelude', source_kind='resource', build_name='HistoricalWriteIdentity', index=ValueRef('CmpClassOrder'), order=None, target=TargetSpec(name='eq_prelude', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='EqMethod', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='capture_path', value=ValueRef('CmpClassId')),)), 'IdentityReset': ContributionSpec(name='IdentityReset', source_name='ResetIdentity', source_kind='resource', build_name='IdentityReset', index=None, order=None, target=TargetSpec(name='comparison_reset', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='capture_path', value=ValueRef('ClassId')),)), 'OrderReset': ContributionSpec(name='OrderReset', source_name='ResetOrder', source_kind='resource', build_name='OrderReset', index=None, order=None, target=TargetSpec(name='order_reset', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=(BindingSpec(kind='external', name='capture_path', value=ValueRef('ClassId')),)), 'DefaultComparison': ContributionSpec(name='DefaultComparison', source_name='ComparisonMethods', source_kind='production', build_name='DefaultComparison', index=None, order=None, target=TargetSpec(name='default_comparison', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=()), 'CurrentComparison': ContributionSpec(name='CurrentComparison', source_name='ComparisonMethods', source_kind='production', build_name='CurrentComparison', index=None, order=None, target=TargetSpec(name='current_comparison', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=()), 'WorkingComparison': ContributionSpec(name='WorkingComparison', source_name='ComparisonMethods', source_kind='production', build_name='WorkingComparison', index=None, order=None, target=TargetSpec(name='working_comparison', paths=(TargetPathSpec(kind='build', path=PathSpec(segments=(PathSegmentSpec(kind='name', name='ClassDef', indexes=()),))),)), bindings=())}
ASSEMBLY_MATCHERS = {'HiddenInitVarAccessors': ContributionMatcherSpec(name='HiddenInitVarAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='InitVars', collection=None),), default_contribution_name='HiddenInitVarAccessor', rules=()), 'ClassDefinitions': ContributionMatcherSpec(name='ClassDefinitions', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name='ClassDefinition', rules=()), 'Results': ContributionMatcherSpec(name='Results', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name='ReturnClass', rules=()), 'Constructors': ContributionMatcherSpec(name='Constructors', inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='required', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('IsLazy'), right=LiteralValueRef(False)))), contribution_name='Required', weight=1.0), ContributionRuleSpec(name='default_value', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(True)))), contribution_name='Default', weight=1.0), ContributionRuleSpec(name='lazy_unset', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('FieldKind'), right=LiteralValueRef('static')), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(False)))), contribution_name='Default', weight=1.0), ContributionRuleSpec(name='factory', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(True)))), contribution_name='Factory', weight=1.0))), 'ConstructorBoundaries': ContributionMatcherSpec(name='ConstructorBoundaries', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name='EmptyConstructorParams', rules=()), 'InitAssignments': ContributionMatcherSpec(name='InitAssignments', inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='init', condition=EqConditionSpec(left=ValueRef('Init'), right=LiteralValueRef(True)), contribution_name='InitAssignment', weight=1.0),)), 'PlainAccessors': ContributionMatcherSpec(name='PlainAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='PlainFields', collection=None),), default_contribution_name='PlainAccessor', rules=()), 'ClassAssignments': ContributionMatcherSpec(name='ClassAssignments', inputs=(AssemblyInputSpec(name='field', collection_name='ClassVars', collection=None),), default_contribution_name='ClassAssignment', rules=()), 'ConstFieldAccessors': ContributionMatcherSpec(name='ConstFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='ConstFields', collection=None),), default_contribution_name='ConstFieldAccessor', rules=()), 'StaticFieldAccessors': ContributionMatcherSpec(name='StaticFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='factory', condition=EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(True)), contribution_name='StaticFactoryAccessor', weight=1.0), ContributionRuleSpec(name='default_value', condition=EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(True)), contribution_name='StaticDefaultAccessor', weight=1.0), ContributionRuleSpec(name='unset', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('HasDefaultFactory'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasDefault'), right=LiteralValueRef(False)))), contribution_name='StaticUnsetAccessor', weight=1.0))), 'MutableStaticSetters': ContributionMatcherSpec(name='MutableStaticSetters', inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='mutable', condition=EqConditionSpec(left=ValueRef('Mutable'), right=LiteralValueRef(True)), contribution_name='MutableStaticSetterContribution', weight=1.0),)), 'ManagedFieldAccessors': ContributionMatcherSpec(name='ManagedFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='ManagedFields', collection=None),), default_contribution_name='ManagedFieldAccessor', rules=()), 'TransientFieldAccessors': ContributionMatcherSpec(name='TransientFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='TransientFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='factory', condition=EqConditionSpec(left=ValueRef('HasWorkingDefaultFactory'), right=LiteralValueRef(True)), contribution_name='TransientFactoryAccessor', weight=1.0), ContributionRuleSpec(name='baseline', condition=EqConditionSpec(left=ValueRef('HasWorkingDefaultFactory'), right=LiteralValueRef(False)), contribution_name='TransientBaselineAccessor', weight=1.0))), 'BindingFieldAccessors': ContributionMatcherSpec(name='BindingFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='BindingFields', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='scalar', condition=EqConditionSpec(left=ValueRef('BindingShape'), right=LiteralValueRef('scalar')), contribution_name='ScalarBindingAccessor', weight=1.0), ContributionRuleSpec(name='map', condition=EqConditionSpec(left=ValueRef('BindingShape'), right=LiteralValueRef('map')), contribution_name='MapBindingAccessor', weight=1.0))), 'LocalStoreFieldAccessors': ContributionMatcherSpec(name='LocalStoreFieldAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='LocalStoreFields', collection=None),), default_contribution_name='LocalStoreFieldAccessor', rules=()), 'ManagedViewAccessors': ContributionMatcherSpec(name='ManagedViewAccessors', inputs=(AssemblyInputSpec(name='field', collection_name='ManagedAccessViews', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='current', condition=EqConditionSpec(left=ValueRef('View'), right=LiteralValueRef('current')), contribution_name='CurrentManagedAccessor', weight=1.0), ContributionRuleSpec(name='thaw', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('View'), right=LiteralValueRef('working')), EqConditionSpec(left=ValueRef('HasThaw'), right=LiteralValueRef(True)))), contribution_name='ThawManagedAccessor', weight=1.0), ContributionRuleSpec(name='working', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('View'), right=LiteralValueRef('working')), EqConditionSpec(left=ValueRef('HasThaw'), right=LiteralValueRef(False)))), contribution_name='WorkingManagedAccessor', weight=1.0))), 'EqPreludeContributions': ContributionMatcherSpec(name='EqPreludeContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='NoEqPrelude', rules=(ContributionRuleSpec(name='view_historical_write', condition=EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), contribution_name='HistoricalWriteIdentity', weight=2.0),)), 'EqGuardContributions': ContributionMatcherSpec(name='EqGuardContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='EqGuard', rules=(ContributionRuleSpec(name='view_indexed', condition=EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), contribution_name='IndexedEqGuard', weight=2.0),)), 'EqIdentityContributions': ContributionMatcherSpec(name='EqIdentityContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='EqIdentity', rules=(ContributionRuleSpec(name='view_indexed', condition=EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), contribution_name='IndexedEqIdentity', weight=2.0),)), 'EqMethodContributions': ContributionMatcherSpec(name='EqMethodContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='EmptyEq', rules=(ContributionRuleSpec(name='tuple', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='TupleEqMethod', weight=1.0), ContributionRuleSpec(name='chain', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='ChainEqMethod', weight=1.0), ContributionRuleSpec(name='empty_tuple', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyTupleEqMethod', weight=1.0), ContributionRuleSpec(name='empty_chain', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyChainEqMethod', weight=1.0), ContributionRuleSpec(name='view_absent', condition=EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(False)), contribution_name='IndexedEmptyEq', weight=2.0), ContributionRuleSpec(name='view_indexed_tuple', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='IndexedTupleEq', weight=2.0), ContributionRuleSpec(name='view_indexed_chain', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='IndexedChainEq', weight=2.0), ContributionRuleSpec(name='view_indexed_empty_tuple', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyTupleEq', weight=2.0), ContributionRuleSpec(name='view_indexed_empty_chain', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpEq'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('UseTupleEquality'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyChainEq', weight=2.0))), 'EqLeftContributions': ContributionMatcherSpec(name='EqLeftContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='EqLeftValue', weight=1.0),)), 'EqRightContributions': ContributionMatcherSpec(name='EqRightContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='EqRightValue', weight=1.0),)), 'HashValueContributions': ContributionMatcherSpec(name='HashValueContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpHashIncluded'), right=LiteralValueRef(True)), contribution_name='HashValueValue', weight=1.0),)), 'EqStepContributions': ContributionMatcherSpec(name='EqStepContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='intermediate', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('CmpLast'), right=LiteralValueRef(False)))), contribution_name='IntermediateEqStep', weight=1.0), ContributionRuleSpec(name='final', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('CmpLast'), right=LiteralValueRef(True)))), contribution_name='FinalEqStep', weight=1.0))), 'LtGuardContributions': ContributionMatcherSpec(name='LtGuardContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='LtGuard', rules=(ContributionRuleSpec(name='view_indexed', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), contribution_name='IndexedLtGuard', weight=2.0),)), 'LtMethodContributions': ContributionMatcherSpec(name='LtMethodContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='NoLt', rules=(ContributionRuleSpec(name='populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='LtMethod', weight=1.0), ContributionRuleSpec(name='empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyLtMethod', weight=1.0), ContributionRuleSpec(name='view_populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='IndexedLt', weight=2.0), ContributionRuleSpec(name='view_empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyLt', weight=2.0), ContributionRuleSpec(name='view_absent', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(False)), contribution_name='IndexedNoLt', weight=2.0))), 'LtLeftContributions': ContributionMatcherSpec(name='LtLeftContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='LtLeftValue', weight=1.0),)), 'LtRightContributions': ContributionMatcherSpec(name='LtRightContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='LtRightValue', weight=1.0),)), 'LeGuardContributions': ContributionMatcherSpec(name='LeGuardContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='LeGuard', rules=(ContributionRuleSpec(name='view_indexed', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), contribution_name='IndexedLeGuard', weight=2.0),)), 'LeMethodContributions': ContributionMatcherSpec(name='LeMethodContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='NoLe', rules=(ContributionRuleSpec(name='populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='LeMethod', weight=1.0), ContributionRuleSpec(name='empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyLeMethod', weight=1.0), ContributionRuleSpec(name='view_populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='IndexedLe', weight=2.0), ContributionRuleSpec(name='view_empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyLe', weight=2.0), ContributionRuleSpec(name='view_absent', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(False)), contribution_name='IndexedNoLe', weight=2.0))), 'LeLeftContributions': ContributionMatcherSpec(name='LeLeftContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='LeLeftValue', weight=1.0),)), 'LeRightContributions': ContributionMatcherSpec(name='LeRightContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='LeRightValue', weight=1.0),)), 'GtGuardContributions': ContributionMatcherSpec(name='GtGuardContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='GtGuard', rules=(ContributionRuleSpec(name='view_indexed', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), contribution_name='IndexedGtGuard', weight=2.0),)), 'GtMethodContributions': ContributionMatcherSpec(name='GtMethodContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='NoGt', rules=(ContributionRuleSpec(name='populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='GtMethod', weight=1.0), ContributionRuleSpec(name='empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyGtMethod', weight=1.0), ContributionRuleSpec(name='view_populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='IndexedGt', weight=2.0), ContributionRuleSpec(name='view_empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyGt', weight=2.0), ContributionRuleSpec(name='view_absent', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(False)), contribution_name='IndexedNoGt', weight=2.0))), 'GtLeftContributions': ContributionMatcherSpec(name='GtLeftContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='GtLeftValue', weight=1.0),)), 'GtRightContributions': ContributionMatcherSpec(name='GtRightContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='GtRightValue', weight=1.0),)), 'GeGuardContributions': ContributionMatcherSpec(name='GeGuardContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='GeGuard', rules=(ContributionRuleSpec(name='view_indexed', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), contribution_name='IndexedGeGuard', weight=2.0),)), 'GeMethodContributions': ContributionMatcherSpec(name='GeMethodContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='NoGe', rules=(ContributionRuleSpec(name='populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='GeMethod', weight=1.0), ContributionRuleSpec(name='empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyGeMethod', weight=1.0), ContributionRuleSpec(name='view_populated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(True)))), contribution_name='IndexedGe', weight=2.0), ContributionRuleSpec(name='view_empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasCompareOperands'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyGe', weight=2.0), ContributionRuleSpec(name='view_absent', condition=EqConditionSpec(left=ValueRef('CmpOrder'), right=LiteralValueRef(False)), contribution_name='IndexedNoGe', weight=2.0))), 'GeLeftContributions': ContributionMatcherSpec(name='GeLeftContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='GeLeftValue', weight=1.0),)), 'GeRightContributions': ContributionMatcherSpec(name='GeRightContributions', inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None), AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='included', condition=EqConditionSpec(left=ValueRef('CmpCompare'), right=LiteralValueRef(True)), contribution_name='GeRightValue', weight=1.0),)), 'HashMethodContributions': ContributionMatcherSpec(name='HashMethodContributions', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), default_contribution_name='EmptyHash', rules=(ContributionRuleSpec(name='generated', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpHash'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasHashOperands'), right=LiteralValueRef(True)))), contribution_name='HashMethod', weight=1.0), ContributionRuleSpec(name='generated_empty', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpHash'), right=LiteralValueRef(True)), EqConditionSpec(left=ValueRef('HasHashOperands'), right=LiteralValueRef(False)))), contribution_name='EmptyHashMethod', weight=1.0), ContributionRuleSpec(name='disabled', condition=EqConditionSpec(left=ValueRef('CmpHashNone'), right=LiteralValueRef(True)), contribution_name='SetHashNone', weight=1.0), ContributionRuleSpec(name='view_disabled', condition=EqConditionSpec(left=ValueRef('CmpHashNone'), right=LiteralValueRef(True)), contribution_name='IndexedHashNone', weight=2.0), ContributionRuleSpec(name='view_untouched', condition=AndConditionSpec(items=(EqConditionSpec(left=ValueRef('CmpHashNone'), right=LiteralValueRef(False)), EqConditionSpec(left=ValueRef('CmpHash'), right=LiteralValueRef(False)))), contribution_name='IndexedEmptyHash', weight=2.0))), 'IdentityResets': ContributionMatcherSpec(name='IdentityResets', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='view_restore', condition=EqConditionSpec(left=ValueRef('RestoreIdentity'), right=LiteralValueRef(True)), contribution_name='IdentityReset', weight=1.0),)), 'OrderResets': ContributionMatcherSpec(name='OrderResets', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), default_contribution_name=None, rules=(ContributionRuleSpec(name='view_restore', condition=EqConditionSpec(left=ValueRef('RestoreOrder'), right=LiteralValueRef(True)), contribution_name='OrderReset', weight=1.0),)), 'ViewComparisons': ContributionMatcherSpec(name='ViewComparisons', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None), AssemblyInputSpec(name='cls', collection_name='Classes', collection=None)), default_contribution_name=None, rules=(ContributionRuleSpec(name='view_default_view', condition=EqConditionSpec(left=ValueRef('CmpClassOrder'), right=LiteralValueRef(0)), contribution_name='DefaultComparison', weight=1.0), ContributionRuleSpec(name='view_current_view', condition=EqConditionSpec(left=ValueRef('CmpClassOrder'), right=LiteralValueRef(1)), contribution_name='CurrentComparison', weight=1.0), ContributionRuleSpec(name='view_working_view', condition=EqConditionSpec(left=ValueRef('CmpClassOrder'), right=LiteralValueRef(2)), contribution_name='WorkingComparison', weight=1.0)))}
ASSEMBLY_EDGES = {'ModuleProduction.classes': AssemblyEdgeSpec(name='ModuleProduction.classes', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='ClassDefinitions'), 'ModuleProduction.results': AssemblyEdgeSpec(name='ModuleProduction.results', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='Results'), 'ClassProduction.constructor_boundary': AssemblyEdgeSpec(name='ClassProduction.constructor_boundary', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='ConstructorBoundaries'), 'ClassProduction.init_params': AssemblyEdgeSpec(name='ClassProduction.init_params', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='Constructors'), 'ClassProduction.init_values': AssemblyEdgeSpec(name='ClassProduction.init_values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='InitAssignments'), 'ClassProduction.values': AssemblyEdgeSpec(name='ClassProduction.values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ClassVars', collection=None),), condition=None, matcher_name='ClassAssignments'), 'ClassProduction.hidden_initvars': AssemblyEdgeSpec(name='ClassProduction.hidden_initvars', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='InitVars', collection=None),), condition=None, matcher_name='HiddenInitVarAccessors'), 'ClassProduction.properties': AssemblyEdgeSpec(name='ClassProduction.properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='PlainFields', collection=None),), condition=None, matcher_name='PlainAccessors'), 'ComparisonMethods.eq': AssemblyEdgeSpec(name='ComparisonMethods.eq', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqMethodContributions'), 'ComparisonMethods.lt': AssemblyEdgeSpec(name='ComparisonMethods.lt', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LtMethodContributions'), 'ComparisonMethods.le': AssemblyEdgeSpec(name='ComparisonMethods.le', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LeMethodContributions'), 'ComparisonMethods.gt': AssemblyEdgeSpec(name='ComparisonMethods.gt', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GtMethodContributions'), 'ComparisonMethods.ge': AssemblyEdgeSpec(name='ComparisonMethods.ge', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GeMethodContributions'), 'ComparisonMethods.hash': AssemblyEdgeSpec(name='ComparisonMethods.hash', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='HashMethodContributions'), 'TupleEqProduction.prelude': AssemblyEdgeSpec(name='TupleEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions'), 'TupleEqProduction.guard': AssemblyEdgeSpec(name='TupleEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions'), 'TupleEqProduction.left': AssemblyEdgeSpec(name='TupleEqProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='EqLeftContributions'), 'TupleEqProduction.right': AssemblyEdgeSpec(name='TupleEqProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='EqRightContributions'), 'ChainEqProduction.prelude': AssemblyEdgeSpec(name='ChainEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions'), 'ChainEqProduction.identity': AssemblyEdgeSpec(name='ChainEqProduction.identity', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqIdentityContributions'), 'ChainEqProduction.guard': AssemblyEdgeSpec(name='ChainEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions'), 'ChainEqProduction.steps': AssemblyEdgeSpec(name='ChainEqProduction.steps', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='EqStepContributions'), 'EmptyTupleEqProduction.prelude': AssemblyEdgeSpec(name='EmptyTupleEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions'), 'EmptyTupleEqProduction.guard': AssemblyEdgeSpec(name='EmptyTupleEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions'), 'EmptyChainEqProduction.prelude': AssemblyEdgeSpec(name='EmptyChainEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions'), 'EmptyChainEqProduction.identity': AssemblyEdgeSpec(name='EmptyChainEqProduction.identity', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqIdentityContributions'), 'EmptyChainEqProduction.guard': AssemblyEdgeSpec(name='EmptyChainEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions'), 'LtProduction.guard': AssemblyEdgeSpec(name='LtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LtGuardContributions'), 'LtProduction.left': AssemblyEdgeSpec(name='LtProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LtLeftContributions'), 'LtProduction.right': AssemblyEdgeSpec(name='LtProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LtRightContributions'), 'EmptyLtProduction.guard': AssemblyEdgeSpec(name='EmptyLtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LtGuardContributions'), 'LeProduction.guard': AssemblyEdgeSpec(name='LeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LeGuardContributions'), 'LeProduction.left': AssemblyEdgeSpec(name='LeProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LeLeftContributions'), 'LeProduction.right': AssemblyEdgeSpec(name='LeProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LeRightContributions'), 'EmptyLeProduction.guard': AssemblyEdgeSpec(name='EmptyLeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LeGuardContributions'), 'GtProduction.guard': AssemblyEdgeSpec(name='GtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GtGuardContributions'), 'GtProduction.left': AssemblyEdgeSpec(name='GtProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GtLeftContributions'), 'GtProduction.right': AssemblyEdgeSpec(name='GtProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GtRightContributions'), 'EmptyGtProduction.guard': AssemblyEdgeSpec(name='EmptyGtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GtGuardContributions'), 'GeProduction.guard': AssemblyEdgeSpec(name='GeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GeGuardContributions'), 'GeProduction.left': AssemblyEdgeSpec(name='GeProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GeLeftContributions'), 'GeProduction.right': AssemblyEdgeSpec(name='GeProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GeRightContributions'), 'EmptyGeProduction.guard': AssemblyEdgeSpec(name='EmptyGeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GeGuardContributions'), 'HashProduction.values': AssemblyEdgeSpec(name='HashProduction.values', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='HashValueContributions'), 'ClassProduction.ConstField_properties': AssemblyEdgeSpec(name='ClassProduction.ConstField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ConstFields', collection=None),), condition=None, matcher_name='ConstFieldAccessors'), 'ClassProduction.StaticField_properties': AssemblyEdgeSpec(name='ClassProduction.StaticField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='StaticFieldAccessors'), 'ClassProduction.mutable_static_setters': AssemblyEdgeSpec(name='ClassProduction.mutable_static_setters', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='MutableStaticSetters'), 'ClassProduction.ManagedField_properties': AssemblyEdgeSpec(name='ClassProduction.ManagedField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedFields', collection=None),), condition=None, matcher_name='ManagedFieldAccessors'), 'ClassProduction.TransientField_properties': AssemblyEdgeSpec(name='ClassProduction.TransientField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='TransientFields', collection=None),), condition=None, matcher_name='TransientFieldAccessors'), 'ClassProduction.BindingField_properties': AssemblyEdgeSpec(name='ClassProduction.BindingField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='BindingFields', collection=None),), condition=None, matcher_name='BindingFieldAccessors'), 'ClassProduction.LocalStoreField_properties': AssemblyEdgeSpec(name='ClassProduction.LocalStoreField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='LocalStoreFields', collection=None),), condition=None, matcher_name='LocalStoreFieldAccessors'), 'ClassProduction.managed_view_properties': AssemblyEdgeSpec(name='ClassProduction.managed_view_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedAccessViews', collection=None),), condition=None, matcher_name='ManagedViewAccessors'), 'ClassProduction.identity_reset': AssemblyEdgeSpec(name='ClassProduction.identity_reset', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='IdentityResets'), 'ClassProduction.order_reset': AssemblyEdgeSpec(name='ClassProduction.order_reset', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='OrderResets'), 'ClassProduction.comparisons': AssemblyEdgeSpec(name='ClassProduction.comparisons', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), condition=None, matcher_name='ViewComparisons')}
ASSEMBLY_PRODUCTIONS = {'ModuleProduction': ComposableProductionSpec(name='ModuleProduction', inputs=(), root=RootSpec(build_name='Root', resource_name='ModuleRoot', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='ModuleProduction.classes', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='ClassDefinitions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ModuleProduction.results', context_inputs=(), from_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), condition=None, matcher_name='Results')))), 'ClassProduction': ComposableProductionSpec(name='ClassProduction', inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), root=RootSpec(build_name='ClassDef', resource_name='ClassBundle', bindings=(BindingSpec(kind='ident', name='class_name_0', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='current_class_0', value=ValueRef('CurrentClassName')), BindingSpec(kind='ident', name='class_name_1', value=ValueRef('ClassName')), BindingSpec(kind='ident', name='working_class_0', value=ValueRef('WorkingClassName')), BindingSpec(kind='ident', name='class_name_2', value=ValueRef('ClassName')))), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.constructor_boundary', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='ConstructorBoundaries')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.init_params', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='Constructors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.init_values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='Fields', collection=None),), condition=None, matcher_name='InitAssignments')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.identity_reset', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='IdentityResets')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.order_reset', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(), condition=None, matcher_name='OrderResets')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.comparisons', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), condition=None, matcher_name='ViewComparisons')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.values', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ClassVars', collection=None),), condition=None, matcher_name='ClassAssignments')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.hidden_initvars', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='InitVars', collection=None),), condition=None, matcher_name='HiddenInitVarAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='PlainFields', collection=None),), condition=None, matcher_name='PlainAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.ConstField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ConstFields', collection=None),), condition=None, matcher_name='ConstFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.StaticField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='StaticFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.mutable_static_setters', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='StaticFields', collection=None),), condition=None, matcher_name='MutableStaticSetters')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.ManagedField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedFields', collection=None),), condition=None, matcher_name='ManagedFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.managed_view_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='ManagedAccessViews', collection=None),), condition=None, matcher_name='ManagedViewAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.TransientField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='TransientFields', collection=None),), condition=None, matcher_name='TransientFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.BindingField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='BindingFields', collection=None),), condition=None, matcher_name='BindingFieldAccessors')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ClassProduction.LocalStoreField_properties', context_inputs=(AssemblyInputSpec(name='cls', collection_name='Classes', collection=None),), from_inputs=(AssemblyInputSpec(name='field', collection_name='LocalStoreFields', collection=None),), condition=None, matcher_name='LocalStoreFieldAccessors')))), 'ComparisonMethods': ComposableProductionSpec(name='ComparisonMethods', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='ComparisonMethods', resource_name='MethodsShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='ComparisonMethods.eq', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqMethodContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ComparisonMethods.lt', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LtMethodContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ComparisonMethods.le', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LeMethodContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ComparisonMethods.gt', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GtMethodContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ComparisonMethods.ge', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GeMethodContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ComparisonMethods.hash', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='HashMethodContributions')))), 'TupleEqProduction': ComposableProductionSpec(name='TupleEqProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='EqMethod', resource_name='TupleEqShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='TupleEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='TupleEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='TupleEqProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='EqLeftContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='TupleEqProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='EqRightContributions')))), 'ChainEqProduction': ComposableProductionSpec(name='ChainEqProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='EqMethod', resource_name='ChainEqShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='ChainEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ChainEqProduction.identity', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqIdentityContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ChainEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='ChainEqProduction.steps', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='EqStepContributions')))), 'EmptyTupleEqProduction': ComposableProductionSpec(name='EmptyTupleEqProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='EqMethod', resource_name='EmptyTupleEqShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyTupleEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyTupleEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions')))), 'EmptyChainEqProduction': ComposableProductionSpec(name='EmptyChainEqProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='EqMethod', resource_name='EmptyChainEqShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyChainEqProduction.prelude', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqPreludeContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyChainEqProduction.identity', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqIdentityContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyChainEqProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='EqGuardContributions')))), 'LtProduction': ComposableProductionSpec(name='LtProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='LtMethod', resource_name='LtShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='LtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LtGuardContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='LtProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LtLeftContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='LtProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LtRightContributions')))), 'EmptyLtProduction': ComposableProductionSpec(name='EmptyLtProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='LtMethod', resource_name='EmptyLtShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyLtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LtGuardContributions')),)), 'LeProduction': ComposableProductionSpec(name='LeProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='LeMethod', resource_name='LeShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='LeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LeGuardContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='LeProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LeLeftContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='LeProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='LeRightContributions')))), 'EmptyLeProduction': ComposableProductionSpec(name='EmptyLeProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='LeMethod', resource_name='EmptyLeShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyLeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='LeGuardContributions')),)), 'GtProduction': ComposableProductionSpec(name='GtProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='GtMethod', resource_name='GtShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='GtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GtGuardContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='GtProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GtLeftContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='GtProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GtRightContributions')))), 'EmptyGtProduction': ComposableProductionSpec(name='EmptyGtProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='GtMethod', resource_name='EmptyGtShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyGtProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GtGuardContributions')),)), 'GeProduction': ComposableProductionSpec(name='GeProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='GeMethod', resource_name='GeShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='GeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GeGuardContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='GeProduction.left', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GeLeftContributions')), InlineApplySpec(edge=AssemblyEdgeSpec(name='GeProduction.right', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='GeRightContributions')))), 'EmptyGeProduction': ComposableProductionSpec(name='EmptyGeProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='GeMethod', resource_name='EmptyGeShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='EmptyGeProduction.guard', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(), condition=None, matcher_name='GeGuardContributions')),)), 'HashProduction': ComposableProductionSpec(name='HashProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='HashMethod', resource_name='HashShell', bindings=()), applies=(InlineApplySpec(edge=AssemblyEdgeSpec(name='HashProduction.values', context_inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), from_inputs=(AssemblyInputSpec(name='operand', collection_name='ComparisonOperands', collection=None),), condition=EqConditionSpec(left=ValueRef('CmpOwner'), right=ValueRef('CmpClassId')), matcher_name='HashValueContributions')),)), 'EmptyHashProduction': ComposableProductionSpec(name='EmptyHashProduction', inputs=(AssemblyInputSpec(name='cmp', collection_name='ComparisonClasses', collection=None),), root=RootSpec(build_name='HashMethod', resource_name='EmptyHashShell', bindings=()), applies=())}
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
