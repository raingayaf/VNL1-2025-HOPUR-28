class ValidationError(Exception):
    """Raised when domain / input validation fails."""

    pass


class DataAccessError(Exception):
    """Raised when reading/writing persistent data fails."""

    pass


class MenuNotFoundError(DataAccessError):
    """Raised when a specific menu cannot be found."""

    pass
