"""Behavior-bearing coordinator states; published selection is separate."""

from .errors import HistoryFaultError, TransactionRequiredError, ReentrantOperationError


class Setup:
    def require_initialized(self):
        raise RuntimeError("history is not initialized")

    def require_write(self):
        raise TransactionRequiredError("managed writes require an active transaction")


class Idle:
    def require_initialized(self):
        pass

    def require_write(self):
        raise TransactionRequiredError("managed writes require an active transaction")


class Editing(Idle):
    def require_write(self):
        pass


class Completing(Idle):
    def require_write(self):
        raise ReentrantOperationError("history is completing")


class Faulted(Idle):
    def require_initialized(self):
        raise HistoryFaultError("history is faulted; recovery requires a new manager")

    def require_write(self):
        self.require_initialized()
