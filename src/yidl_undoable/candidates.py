"""A frozen complete graph presented to validators before any publication."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CandidateRead:
    fields: object
