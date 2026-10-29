# Troubleshooting

| Symptom | Check and remedy |
| --- | --- |
| Cannot begin, navigate or snapshot after construction | Call `history.initialize(*roots)` once with at least one same-manager root. Construction alone does not establish history. |
| Managed setter raises `TransactionRequiredError` | Begin an edit on the owning manager; current/pinned views remain read-only. |
| A cache or label survives rollback | Ordinary/local/lazy/constant storage is nonversioned; declare reversible values as `managed`. |
| Mutable/custom value raises `FrozenValueError` | Convert to the supported stable surface with `freeze`; use `thaw` for its editable working form. |
| Retained child raises `ObjectAbsentError` | It is absent from the selected managed graph. Navigate to a frame where it is present or choose the documented absent-read policy. |
| `UnavailableNodeError` after failed construction/edit | No surviving visible baseline exists for that node; do not resurrect aborted or future-only creations. |
| A retained `.current` changes | It is a live view. Keep a `FrameSnapshot` for pinned committed managed data. |
| Redo disappeared | A new successful commit after undo replaces the redo tail, including no-op commits. |
| Nested rollback cancels more than the inner block | Same-manager nesting joins; it does not create savepoints. |
| A factory's input is unknown or unresolved | Parameter names select providers; check spelling, cycles, lazy defaults and opt-in self ordering. |
| Validation failed but preview remains editable | `validate()` keeps the edit open for repair; final commit failure aborts it. |
| Callback mutation raises `ReentrantOperationError` | Keep callbacks pure; perform changes outside their factory/converter/validator invocation. |
| A model cannot be hashed | `eq=True` deliberately makes all its facades unhashable. |
| A cache hit does not appear | Inspect [cache diagnostics](Cache.md); check startup environment, identity and storage trust/availability. |
| Windows CPython 3.15 install lacks an Astichi wheel | See [installation qualification](GettingStarted.md#installation); a source build is not qualified here. |

## Known declaration limitation

A field named `schema` currently collides with a generated capture and fails
during decoration. Use another name. The integration preserves that existing
limitation; it does not claim arbitrary field-name support.

`HistoryFaultError` means unexpected backend ownership/completion evidence. There
is no recovery/reset operation; consult [the failure reference](API.md#absence-snapshots-and-failures)
without assuming an unconfirmed publication is safe to use. The manager does not
guarantee concurrent thread/task isolation or reversal of external side effects.
