"""Independent installed comparison/history/context subset."""
import contextvars,json,os,pathlib,sys
os.environ['ASTICHI_LOWER_ENGINE']=sys.argv[1]
import astichi,yidl,yidl_lifecycle,yidl_undoable as p
from astichi.lower_engine.native import select_lower_engine
selection=select_lower_engine()
assert selection.selected_engine==sys.argv[1] and selection.fallback_scope is None
for module in (astichi,yidl,yidl_lifecycle,p):
 assert pathlib.Path(module.__file__).resolve().is_relative_to(pathlib.Path(sys.prefix).resolve())
@p.undoable(eq=True,order=True)
class Child:
 value:int=p.managed(default=1)
 cache:dict=p.local_store(default_factory=dict)
@p.undoable
class Parent:
 child:object=p.managed()
 identity:object=p.managed(write_compare='identity')
history=p.UndoRedoManager()
a=Child(transaction_manager=history);b=Child(transaction_manager=history)
parent=Parent(transaction_manager=history,child=a,identity=a)
history.initialize(parent,a,b)
assert a==b and not (a<b)
a.cache['noise']=1;assert a==b
try:hash(a)
except TypeError:pass
else:raise AssertionError('structural facade unexpectedly hashable')
assert Child.__eq__(a,b.current) is NotImplemented
history.begin();parent.working.child=b
assert (parent.node_id,'child') in history._edit.touched
old=parent.working.identity;parent.working.identity=old
assert (parent.node_id,'identity') not in history._edit.touched
parent.working.identity=parent.current.identity
assert (parent.node_id,'identity') in history._edit.touched
history.commit()
assert parent.child.node_id==b.node_id
assert history.undo() and parent.child.node_id==a.node_id
assert history.redo() and parent.child.node_id==b.node_id
from yidl_undoable.write_comparison_context import _historical_write_equal,_historical_write_scope
saved=[]
class Opaque:
 def __eq__(self,other):
  assert other is right
  marker=_historical_write_scope.get()
  assert marker is not None and marker.active and marker.__slots__==('active',)
  saved.append(contextvars.copy_context())
  return a==b
left=Opaque();right=object()
assert history._call('owner installed native value comparison',lambda:_historical_write_equal(left,right)) is False
assert _historical_write_scope.get() is None
assert a==b and saved[0].run(lambda:a==b)
class Cancel(BaseException):pass
class Raises:
 def __eq__(self,other):
  saved.append(contextvars.copy_context())
  raise Cancel('owner cancellation')
try:history._call('owner installed cancellation',lambda:_historical_write_equal(Raises(),object()))
except Cancel:pass
else:raise AssertionError('cancellation suppressed')
assert _historical_write_scope.get() is None and saved[1].run(lambda:a==b)
print(json.dumps({'python':sys.version.split()[0],'backend':sys.argv[1],
 'structural_options_and_management_exclusion':'pass','distinct_equal_child_history':'pass',
 'identity_write_reference_behavior':'pass','closed_copied_context_and_baseexception':'pass',
 'scope':'Owner installed bounded E/F subset; complete callback/context/installed corpus separate'}))
