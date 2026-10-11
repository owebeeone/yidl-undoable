"""Declaration recognition must include lazily exposed class annotations."""

from yidl_undoable import managed
from yidl_undoable.undoable_harvester import harvest_undoable_definition


def test_harvester_reads_local_annotations_through_the_language_api():
    class Declaration:
        value: int = managed(default=0)

    schema = harvest_undoable_definition(Declaration)
    assert tuple(fact["field_name"] for fact in schema.fields) == ("value",)
    assert schema.annotations["value"] is int
