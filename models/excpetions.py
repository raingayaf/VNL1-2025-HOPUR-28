class ValidationError(Exception):
    """Raised when domain / input validation fails."""

    pass


class DataAccessError(Exception):
    """Raised when reading/writing persistent data fails."""

    pass


class MenuNotFoundError(DataAccessError):
    """Raised when a specific menu cannot be found."""

    pass


class FormatError(ValidationError):
    """Raised when specific input is in wrong format(email, date, etc.)"""

    pass


class OutOfRangeError(ValidationError):
    """Raised when input requires specific range but input is outside allowed limits"""

    pass


class DuplicateEntryError(ValidationError):
    """Raised when something already exists and must be unique"""

    pass


class PermissionDeniedError(DataAccessError):
    """raised when user is not allowed access to resource"""

    pass
