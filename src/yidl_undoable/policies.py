"""The two supported absent-read behaviors; custom policies are deferred."""

from abc import ABC, abstractmethod
from bisect import bisect_right
from .errors import ObjectAbsentError


class AbsentReadPolicy(ABC):
    @abstractmethod
    def resolve(self, node_id, selection):
        raise NotImplementedError


class RaiseAbsent(AbsentReadPolicy):
    def resolve(self, node_id, selection):
        raise ObjectAbsentError(
            f"node {node_id} absent at frame {selection.frame.frame_id}"
        )


class ReadLastVisible(AbsentReadPolicy):
    def resolve(self, node_id, selection):
        history = selection.epoch.nodes.get(node_id)
        if history is not None:
            position = bisect_right(history.presence, selection.frame.frame_id) - 1
            if position >= 0:
                return history.presence[position]
        raise ObjectAbsentError(
            f"node {node_id} has no prior visible frame at {selection.frame.frame_id}"
        )
