# Adversarial review of Undoable documentation and generation claims

Date: 2026-10-29.

**Verdict: GO for the reviewed documentation and the bounded specialized/cache
integration claims identified below.** No blocking findings remain after the
corrections recorded here. This is not a package release authorization or a new
platform-wide qualification. The current-main cache additions remain explicitly
unreleased relative to published 0.1.1.

## Scope and provenance

The user requested the Lifecycle documentation format for Undoable, independent
adversarial review before push, and separately authorized integration of the
specialized/cached normal decorator using existing tests. The documentation
specification and `dev-docs/SpecializedAccessorIntegration.md` record those two
boundaries. Implementation authority does not arise merely from a documentation
preference.

This review covers public documentation/examples, site configuration/helpers and
workflow, and the normal-decorator specialized/cache seam supporting their
claims. It reads the relevant runtime, generated accessors, cache identity and
binding code, and focused tests. SDK, Lifecycle, Cache and Dataclass implementation
remain reference-only. No new architecture or cross-repository implementation
is required by a finding. This reviewer edits only this report and performs no
commit, push, deployment, package publication or environment mutation.

Baseline: `307c0ff6924b5c405f2d287b14448d0006cfe35a`. The candidate includes
authorized implementation changes as well as documentation; the review is not
represented as a docs-only implementation diff. The public documentation
manifest and bounded seam-file digests below identify the reviewed state.

## Findings, ranked by severity

### R1 — P1, resolved: new cache APIs were presented on the published install route

Initially the README, Cache page, API and architecture described the specialized
normal decorator and compiled-builder controls without a release boundary,
alongside `pip install yidl-undoable`. An independent probe of installed
`yidl-undoable==0.1.1` found
`find_spec("yidl_undoable.code_cache") is None`. Consequently the advertised cache
import snippet fails on that published installation. Existing core examples
remain valid; this finding concerns unavailable new APIs and implementation.

The minimal remedy was documentation qualification, since a package release is
outside this delivery. README, `docs/Cache.md:3–5`, API and architecture now label
specialization/caching as current-main additions absent from published 0.1.1.
The Cache page directs readers to the checkout for those controls. Reassessment
accepts this explicit boundary; no dependency release or library redesign is
required. The site must retain these labels until a separate package release.

### R2 — P2, resolved: reference omitted marker option signatures/defaults

The initial API described itself as the complete contract but did not give
accepted options/defaults for each marker. In particular, callers could not look
up `init`, `allow_self_factory`, lazy `mutable`, transient working factories, or
the distinction between logical `compare` and managed `write_compare` without
source inspection. This fell short of the requested detailed reference format.

`docs/API.md` now includes descriptive signatures for all marker families, the
`static` alias and validator decorator, plus a shared option/constraint table.
These were checked against `undoable_markers.py`, the underlying Lifecycle marker
factories and Undoable harvesting. The reference explains wrapper signatures,
keyword-only construction, explicit versus omitted write-compare policy,
excluded comparison families, self opt-in and factory signature restrictions.
The opening now distinguishes literal default references from factory policy,
avoiding the former implication that every default is independently copied.

### R3 — P2, resolved: a new nullable-conversion claim copied Lifecycle semantics

During R2 remediation the new option table said optional-None managed values
bypass `freeze`/`thaw` conversions. That is false for Undoable. A focused source
probe using `value: int | None = managed(default=None, freeze=record,
thaw=record)` recorded `freeze(None)`, `thaw(None)`, then `freeze(None)` across
initialization and a working read/commit. `_candidate` and `_read_managed` invoke
the supplied conversions without Lifecycle's optional-None bypass.

The table now explicitly says nullable-aware converters must handle None and
Undoable passes None to a provided converter. No runtime change was made or
needed. This correction also reinforces the requested separation of each
package's callback conventions.

### Remaining blockers

None established. Nonblocking limits are recorded below rather than promoted
into new implementation prerequisites.

## Documentation and runtime contract review

The learning route stands alone: a concrete edit/undo/redo example precedes
rollback versus navigation, managed/nonversioned storage, live views, collection
conversion, graph membership, snapshots, providers and validation. Readers do
not need Lifecycle or YIDL knowledge. Examples expose retained-view behavior and
abandoned redo branches. This is learning-design judgment, not experimental
evidence of retention improvement.

The reviewed graph and history claims agree with the existing runtime: managed
edges establish membership; ordinary fields and caches do not; roots move with
frames; aliases are permitted but cycles/cross-manager graphs are rejected;
provisional attachment and unusable future/aborted baselines are distinguished
from reattachment of previously visible nodes. Live views follow selection and
snapshot nodes pin committed managed data, including aliases, without capturing
application methods or nonversioned fields. Joined nesting is not a savepoint,
and a successful no-op outer commit still creates a frame.

Undoable-specific callback distinctions are accurate after R3: factories receive
the generated model `cls`; transient working factories use generic named
providers and opt-in accessing-facade `self`, rather than Lifecycle's special
current/working injection; local-store factories are zero-argument; conversion
callbacks receive one positional value. Full rooted-candidate validation includes
untouched nodes and accepts any result other than exact False, unlike Dataclass's
strict validator-result contract. Candidate managed reads stay on frozen
candidate data. No borrowed Lifecycle participant-only validation promise remains.

The stable-value/working-container guide correctly limits immutability and
explains detached escaped working data. Snapshot and absence policies are
appropriately bounded. The comparison guide distinguishes optional structural
facade equality from managed write detection and retains the historical identity
rule during value-write comparison callbacks. The existing detailed API remains
available at its original URL; the architecture URL is preserved as an updated
internals reference. Installation flags the known Windows CPython 3.15 Astichi
wheel limitation without claiming an untested source build is qualified.

## Specialized accessor and cache seam

Inspection of `undoable.py` confirms that the normal decorator chooses the shipped
specialized builder. The separate experimental adapter compiles authored YIDL for
probe/regeneration coverage; normal decoration does not require that compilation
or runtime Dataclass authority. Field-specific authored accessors preserve
history selection for managed values and use existing construction/provider,
callback fence and nonversioned mechanisms where appropriate.

The cache stores compiled builder code, with source inspection text attached as
inert constants. On every hit/miss the decorator creates a fresh namespace and
capture capsule, executes the builder code, and binds the current schema and user
base. Runtime defaults, annotations, factories, conversions, keys and methods are
not embedded into the structural digest. Their derived generation-shape facts
are included; unknown field-schema shapes bypass. The digest also includes
comparison/restoration choices and Astichi environment inputs. Producer source
inventory is captured before generation, and reuse goes through the existing
YIDL Cache trust, identity and storage policy.

Focused tests demonstrate cold generation, an in-process hit, a fresh-process
disk hit with assembly forbidden, runtime annotation/default/callback binding,
fresh class identity, changed structural digest, disabled caching, unusable-root
bypass and explicit maintenance. Source survives hits. No stale binding or
cached live-class defect was established in this bounded seam review.

These claims do not establish a general speedup, reduced commit cost, stronger
history algorithm, thread isolation or hot reload. The docs correctly separate
the original experiment, accessor experiment and cache probe workloads. Producer
invalidation uses the shared cache inventory contract; the narrow consumer tests
do not themselves re-prove every shared cache storage/invalidation case. That is
a verification limit, not a demonstrated defect requiring SDK changes.

The documented `schema` field-name collision remains an existing limitation.
Discovery does not authorize fixing it in this delivery, and the guides do not
claim arbitrary-name support.

## Independent checks

Reviewer execution used CPython 3.12.12 and installed registry dependencies with
the source checkout selected only for Undoable implementation checks, using
`PYTHONPATH=src ASTICHI_LOWER_ENGINE=python`:

- Eight complete examples and eighteen guide blocks passed.
- `tests/test_code_cache.py` and `tests/test_specialized.py`: **38 passed**.
- Focused probes confirmed generated `cls`, retained initvars plus direct
  field/classvar transient working providers, opt-in working-facade `self`,
  complete validation of an untouched rooted candidate, and R3's None conversion
  behavior.
- Separately, all eight example programs passed against installed published
  Undoable 0.1.1 without source selection. Its cache module absence was verified
  independently. The current-main Cache guide block is intentionally outside
  that published package's supported surface and is now labeled accordingly.
- Final strict MkDocs build, site checks and whitespace checks passed: 14 HTML
  pages, 434 local links/assets, 35 search entries.

The parent separately runs the full existing version/backend matrix. This report
does not present those parent runs as independent reviewer executions, nor does
it substitute focused seam tests for the parent's required regression completion.
No broad new benchmark or architecture project is required by this review.

## Site and publication boundary

The workflow installs the packaged checkout, executes examples, builds strictly,
checks public links/assets/search/exclusions, then uploads the artifact. Its
deploy job is gated to the canonical repository's main branch outside pull
requests after build success. Actions are pinned, and Pages/OIDC write access is
confined to deploy. Development/validation records stay out of public site/search;
repository-only links resolve back to source. Package publication is separate.

This review does not perform or verify live Pages deployment/environment settings.
The parent retains authorized publication and live-site verification work after
the regression gate. No SDK implementation change or package release is implied
by this GO.

## Reviewed file identity

The following manifests are generated from sorted repository-relative file paths,
each line containing SHA-256, two spaces, path and LF. Public documentation/site/
example files are separated from the bounded implementation seam. This report
is excluded because authoring it changes its bytes. Subsequent substantive
changes to a reviewed file require reassessment.

### Public documentation candidate

Manifest SHA-256: `8b9414ec5cdcaea48281ad064e6d2891400201025328e3cd852905145263e4c8`.

```text
3284540d0ae81972e4ff385a3a13460700ef34fe18438a38f5be4306a0f23cb6  .github/workflows/docs.yml
b030fe74b6f1fa6f45853459c375d6bc3d198fc6e6478fa08be7d29f4c2d9857  CONTRIBUTING.md
228f26aeea3f1966f119963e26808b2b72462a1e00b603c4fe3bbbadbe634de9  README.md
82af0f523fad482c0922f804db8d026696a0376c52fab81f8f5eee62407781bf  dev-docs/documentation/Specification.md
e01b572063613781c5d5ba0fb49454bd783662997f4b28b20908ce3a8645110c  dev-docs/documentation/check_site.py
d3b17e95db69314c5d7d37f8c6239f78864f95530a53e8f5dc508426bfd9b006  dev-docs/documentation/site_hooks.py
7770b4f0f75dfc1f0454205715b0c8b6d26005c14230b77f38569ba0c1cb25ee  dev-docs/documentation/verify_examples.py
dcaede80d4840150535ddacd7723e95b04bd604f12dbf7605dc63acd51dfb182  docs-requirements.txt
66020e129609fab2d069fcf672af0a260aed9fe2b799d2d90670b6a16909b14e  docs/API.md
ebcab688e38fcbaf7875108031627f36f7a6664e7797b1e6fe805dac28f07e9c  docs/Architecture.md
d02eb56522de5ceb2800b89127327fccf81649ea017fe1cf637d7fe231beb64a  docs/Cache.md
b9cbf9199126e60076098ca2d072d2c2b7ac28d2974b5761d28e203a10598d53  docs/Collections.md
6165e69bfe6ed24568c0e82a7270416ea519f58cabc3eb5f3e97ea6f0369ab75  docs/Comparisons.md
49393461f11fa08592a9f1f77267533dd4bff28075e7f7e8307e07baa963ee08  docs/Concepts.md
1cc45c5f9d14b5b02f693b9d582d630decae349fdc0b018f6854ffc505ca3576  docs/GettingStarted.md
994817f65869cc0c6f186452d887747b34037c87b14581b2a71de463ad13db57  docs/Initialization.md
6c574bf729e2681a50efd511cd55616f5e702497dec9d79825241bb758516a6d  docs/ObjectGraphs.md
ea4e164fdb4a7e832c6156a321e33fbbdd42d88a94c867dcc248295f4f797a90  docs/Snapshots.md
34e6d6086111e764e388c4b3062f41851a3fdce71bb64921813b4242b882d567  docs/Transactions.md
fe9aaebbd31a1ad462d55fbfb393b6b7ee25707eda6dcaaccfc7fb9855e04c8b  docs/Troubleshooting.md
871b20f9565f367470c7dbffcf0bc8efdaa381478ccf4e42320063f94ee079ce  docs/index.md
616e4ddaa48ded2ee0fb9a13ecbb01a575de6265283cde1fa1f46e0de98d3b80  examples/README.md
13fe22a5c35c09a92c97297caafac9240722cbcc575add7871317026a0ca29da  examples/collections.py
03aebc4bd26d6438640a508f8e65947c33f3703deec4d4485edfbd90115e534a  examples/dependent_fields.py
bf031dbabee1cd702d4a040073e2080a050490f5cf08adc3edcd34612cf47038  examples/field_boundaries.py
d5a477f669d86ad1dd0cb5c65f322fcbd937841a364717e2d002fe578b1ca9d9  examples/first_use.py
d4312cf0e5a3d6ef5df73d68ce6e80f841b95a1e527541fc56b4fe3fbc1438fc  examples/nested.py
307cbb01ecffa1b8571f448146b94935c7aa399458e203896ac6e03e7a995090  examples/object_graphs.py
62a5dc76d40be147e6976b4706a8f880b04df9d09a99cafe31de242e1c908ac7  examples/snapshots.py
8c1db71ee89c679d5ff01f90e9ab74abfc0a5b1319dc35860871cdce2d1c38d1  examples/validation.py
36964a5ff24545c26dc9892d8414734b39103a4e1947c66326ad92ff6e5a7962  mkdocs.yml
```

### Specialized/cache seam

Manifest SHA-256: `fffb88462e404df8ea796dc0ac70a89de1efb3b97ee0730fd41272c022aea9fd`.

```text
43ff8fc9b51e2efef12d2967fe0756a7b1899ff56878a492b714117bccb40c4e  src/yidl_undoable/_generated_specialized_base.py
9454a0c847419625b1e5d39d4d8044c2163af85db9afdbe9d12f311c32572e93  src/yidl_undoable/accessor_captures.py
db0b0abdbb21d135b039ed503ff9f10f74a3f0aed469e003c8e205cf1d4f50fd  src/yidl_undoable/code_cache.py
1a98c6e3a797d26bd87fe7bb11e5f2f4c5bdc0b0f6e4d80f173181de6584c3e5  src/yidl_undoable/code_cache_inputs.py
b5d6d530f9a540d4e812baa95a6e8ba6b96df0fa48a3baccfca9e82e738daaa5  src/yidl_undoable/undoable.py
781b7644e16fb8e918bb6a3186d9ea9c50a231aff1191c126a387dcfcbcd8a94  src/yidl_undoable/yidl/experimental/specialized.yidl
a99ae8532608b4525c0c50a6560af45fc1c0ab64aefbe38c9d689c3fa73e11e2  tests/cache_scenario.py
3e35959dc441bd2277b8b262eb691faebc636c0270fbd85d21b8e4efb37cb205  tests/test_code_cache.py
ec9910e160b62def2a853b4d4245303097370f53aa287f83485c43928f42cb5b  tests/test_specialized.py
```
