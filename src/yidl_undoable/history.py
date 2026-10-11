"""Immutable sparse storage. Epoch replacement is the only publication boundary."""

from bisect import bisect_right
from dataclasses import dataclass
from types import MappingProxyType
from .errors import UnavailableNodeError


@dataclass(frozen=True, slots=True)
class FieldHistory:
    frame_ids: tuple = ()
    values: tuple = ()

    def at(self, frame_id):
        index = bisect_right(self.frame_ids, frame_id) - 1
        if index < 0:
            raise UnavailableNodeError(f"no field baseline at frame {frame_id}")
        return self.values[index]

    def trim(self, frame_id):
        stop = bisect_right(self.frame_ids, frame_id)
        return FieldHistory(self.frame_ids[:stop], self.values[:stop])


@dataclass(frozen=True, slots=True)
class FrameRecord:
    frame_id: int
    roots: tuple
    present: frozenset


@dataclass(frozen=True, slots=True)
class NodeHistory:
    schema: object
    fields: object
    presence: tuple


@dataclass(frozen=True, slots=True)
class HistoryEpoch:
    nodes: object
    frames: tuple


@dataclass(frozen=True, slots=True)
class PublishedSelection:
    epoch: HistoryEpoch
    cursor: int

    @property
    def frame(self):
        return self.epoch.frames[self.cursor]


@dataclass(frozen=True, slots=True)
class PreparedCommit:
    selection: PublishedSelection


def immutable(mapping):
    return MappingProxyType(dict(mapping))
