"""Custom exceptions used across the heritage application."""


class HeritageError(Exception):
    """Base class for all application-level errors."""


class ValidationError(HeritageError):
    """Raised when user input is missing or in the wrong format."""


class PermissionDenied(HeritageError):
    """Raised when the current role is not allowed to perform an action."""


class RecordNotFound(HeritageError):
    """Raised when a requested record ID does not exist."""


class StorageError(HeritageError):
    """Raised when the database cannot complete an operation."""
