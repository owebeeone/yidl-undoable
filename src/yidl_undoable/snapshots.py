"""Data-only handles pinned to an immutable epoch, with nested alias identity."""

from dataclasses import dataclass, field
from .values import decode
from .errors import ObjectAbsentError


@dataclass(frozen=True, slots=True)
class FrameSnapshot:
    _epoch: object
    _frame: object
    _cache: dict = field(default_factory=dict, repr=False, compare=False)

    @property
    def frame_id(self):
        return self._frame.frame_id

    @property
    def roots(self):
        return tuple(self.node(n) for n in self._frame.roots)

    def node(self, node_id):
        if node_id not in self._frame.present:
            raise ObjectAbsentError(
                f"node {node_id} absent in snapshot frame {self.frame_id}"
            )
        if node_id not in self._cache:
            self._cache[node_id] = SnapshotNode(self, node_id)
        return self._cache[node_id]


@dataclass(frozen=True, slots=True, eq=False)
class SnapshotNode:
    _snapshot: FrameSnapshot
    node_id: int

    def __eq__(self, other):
        return (
            isinstance(other, SnapshotNode)
            and self._snapshot is other._snapshot
            and self.node_id == other.node_id
        )

    def __hash__(self):
        return hash((id(self._snapshot), self.node_id))

    def get(self, field_name):
        fields = self._snapshot._epoch.nodes[self.node_id].fields
        if field_name not in fields:
            raise AttributeError(
                f"{field_name}: snapshot exposes only declared managed fields"
            )
        return decode(
            fields[field_name].at(self._snapshot.frame_id), self._snapshot.node
        )
