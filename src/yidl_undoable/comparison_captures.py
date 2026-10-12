"""Immutable generation captures; direct authored references, never name dispatch."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ComparisonCaptures:
    scope: object
    equal: object
    hash_function: object
    less: object
    less_equal: object
    greater: object
    greater_equal: object


def capture_ids(public_name):
    """Private association IDs must avoid every generated lexical class binding."""
    public = {public_name, public_name + "_Current", public_name + "_Working"}
    index = 0
    while True:
        prefix = f"_u_capture_{index}"
        identifiers = (
            prefix,
            *(prefix + "_" + view for view in ("default", "current", "working")),
        )
        if public.isdisjoint(identifiers):
            return identifiers
        index += 1
