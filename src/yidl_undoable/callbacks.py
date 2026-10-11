"""Application calls own their original context across nested provider reads."""

from dataclasses import dataclass
from .errors import ReentrantOperationError, HistoryFaultError
from .states import Completing, Faulted


@dataclass(frozen=True, slots=True)
class OperationContext:
    selection: object
    edit: object
    state: object
    token: object
    begin_count: int
    token_id: object
    token_key: object

    def intact(self, manager):
        token = manager._backend.active_transaction
        return (
            manager._selection is self.selection
            and manager._edit is self.edit
            and manager._state is self.state
            and token is self.token
            and manager._backend.begin_count == self.begin_count
            and (
                token is None
                or (token.tx_id == self.token_id and token.tx_key is self.token_key)
            )
        )


def capture(manager):
    token = manager._backend.active_transaction
    return OperationContext(
        manager._selection,
        manager._edit,
        manager._state,
        token,
        manager._backend.begin_count,
        None if token is None else token.tx_id,
        None if token is None else token.tx_key,
    )


def call(manager, context, function):
    owner = capture(manager)
    manager._callback_depth += 1
    try:
        result = function()
    except BaseException as exc:
        exc.add_note(context)
        if not owner.intact(manager):
            manager._fault("application callback lost operation ownership")
            raise HistoryFaultError(context + ": operation ownership lost") from exc
        raise
    finally:
        manager._callback_depth -= 1
    if not owner.intact(manager):
        manager._fault("application callback lost operation ownership")
        raise HistoryFaultError(context + ": operation ownership lost")
    return result


def require_mutation(manager):
    if manager._callback_depth or isinstance(manager._state, Completing):
        raise ReentrantOperationError(
            "same-manager mutation from an application callback/completion"
        )
    if isinstance(manager._state, Faulted):
        manager._state.require_initialized()
