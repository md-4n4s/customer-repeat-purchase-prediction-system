class MissingRequiredFieldException(Exception):
    """Raised when a required field is missing."""


class InvalidFieldException(Exception):
    """Raised when a field contains invalid values."""


class InvalidFieldTypeException(Exception):
    """Raised when a field has an invalid data type."""
