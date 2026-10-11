# Independent verification evidence

Status: independent checks passed; runtime review pending. Paths below are repository-relative;
external temporary environment prefixes are omitted from commands/results.

Pinned dependency wheels were built independently from the accepted design's
source tuple: Astichi 1.1.3, YIDL 0.1.0, YIDL Cache 0.1.0 and Lifecycle 0.1.0.
Each matrix environment is a separate noneditable installation of those wheels,
with native engine loading explicitly confirmed. No adjacent source changes.

## Initial settled-draft checks

| Python | `python -m pytest -q` from member root | Installed wheel examples + base check from unrelated cwd, `python -I` |
| --- | --- | --- |
| 3.12.12 | 43 passed in 8.04s | Both examples passed; generated base matches. |
| 3.13.12 | 43 passed in 8.97s | Both examples passed; generated base matches. |
| 3.14.3 | Collection fails: native materialization did not produce a composable. | Pending investigation; no claim of compatibility. |

`uv build yidl_undoable --out-dir <temporary wheelhouse>` succeeded, building the
wheel from its sdist. Content inspection found all nine YIDL resources, generated
base and `py.typed` in the wheel; sdist includes resources and canonical tests.
The drafter is investigating the 3.14 failure under its original source ownership.
Final artifact hashes and supported-version disposition follow below after closure.

## Final corrected-source verification

The Python 3.14 failure was annotation recognition, not native engine loading:
deferred class annotations were absent from the raw class dictionary. A real
failing recognition regression preceded the fix to `inspect.get_annotations`.
No dependency source changes, engine fallback, or version restriction was used.

| Python | Independent full source suite | Final installed wheel, isolated imports |
| --- | --- | --- |
| 3.12.12 | 44 passed in 7.75s | Both examples passed; generated base matches; import resolves inside environment. |
| 3.13.12 | 44 passed in 8.52s | Both examples passed; generated base matches; import resolves inside environment. |
| 3.14.3 | 44 passed in 8.14s | Both examples passed; generated base matches; import resolves inside environment. |

Source tests run from this repository with separate noneditable dependency wheel
installations. Wheel smoke runs from an unrelated temporary directory using
`python -I examples/first_use.py`, `python -I examples/nested.py` (script paths
resolved from this repository), and
`python -I -m yidl_undoable.regenerate_undoable_base`. Import isolation is checked
against the environment prefix. Native Astichi loading succeeds on all versions.

Final independent `uv build` succeeds from sdist. SHA-256:

- `yidl_undoable-0.1.0-py3-none-any.whl`: `227a61c3bac4b7dd4a58706fccd629df4e90e6923e1a9c4833e175cc893ab792`
- `yidl_undoable-0.1.0.tar.gz`: `b62767d2dae8b9513510874041f92f48be520a32f88b274370797c2052597ec1`

Wheel installs use pinned, locally built dependency wheels, then the Undoable
wheel with `--no-deps`. Lifecycle is not yet published to the package registry;
these checks establish the pinned source tuple, not public registry installation
or a release. Nine YIDL resources, generated base and `py.typed` are packaged;
the sdist also includes canonical tests. All checks above precede runtime review.

## First runtime gate

Passing tests and wheels did not establish acceptance. At `a97e43e`, independent
Code/Surface found three P2s and State found four P2s. They do not overlap.
Reports are filed verbatim in this directory. All seven are assigned to one
bounded test-led remediation; runtime remains NO-GO until counterexamples close.

## Remediation cycle 1 independent checks

The merged revision adds five canonical stories and narrow fault/provider tests.
It implements the seven original counterexamples without changing the accepted
public API/design. Independent full-source suite:

| Python | Result | Rebuilt wheel examples/regeneration/import isolation |
| --- | --- | --- |
| 3.12.12 | 55 passed in 7.49s | All passed. |
| 3.13.12 | 55 passed in 8.13s | All passed. |
| 3.14.3 | 55 passed in 8.04s | All passed. |

Independent wheel-from-sdist build passed; SHA-256 for this correction artifact:

- Wheel: `ed94e99762462b11f6f91e1f205599ea0cb2681f753b6af8707ef5eb8b5a34c7`
- Sdist: `e980082a8b5ad03137c262809acae99995b5fbee0f2afc421ea7ef1b751847f8`

These artifacts replace the earlier runtime draft artifacts. Native pipeline,
pinned dependency tuple, installation isolation and no-registry-release limits
remain as stated above. Absolute machine-path scan returned no matches and
`git diff --check` passed. Passing checks still require reviewer closure.

## Second runtime gate

At `72e1433`, both reviewers independently closed the seven original findings,
but reported three bounded additional P2s. The complete reports are filed
verbatim as `UndoableImplementation-ReviewCode-2.md` and `-ReviewState-2.md`.
The 55-test matrix/wheel evidence remains true for that object; runtime acceptance
is blocked until cycle2 closes provisional reads/fencing and full begin setup.

## Remediation cycle 2 independent checks

| Python | Full source suite | Rebuilt installed-wheel examples/base/import isolation |
| --- | --- | --- |
| 3.12.12 | 89 passed in 6.98s | All passed. |
| 3.13.12 | 89 passed in 7.62s | All passed. |
| 3.14.3 | 89 passed in 7.68s | All passed. |

Independent wheel-from-sdist build succeeds. Final runtime-correction SHA-256:

- Wheel: `ac593d36154e3a6df39e1e92d92f9033ecdc3b4ca004bb2fc574f8f044c951e3`
- Sdist: `cfd16922b2e7a8ca73841cbfddc9d71f51372fa7274fc2380ebd2ef0155a8494`

The source tuple, isolated pinned dependency wheels and native engine remain
unchanged. No adjacent source edits, platform fallback or version restriction.
These artifacts supersede earlier draft artifacts; later evidence-only commits
may update documentation without changing tested runtime bytes. Machine-path
scan has no matches and whitespace check passes. Runtime review still pending.
