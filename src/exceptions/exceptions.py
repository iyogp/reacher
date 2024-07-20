from requests import HTTPError


class ArgumentInputNotParsedError(ValueError):
    """Raised when an argument is not parsed correctly."""
    pass


class EnvironmentInputNotParsedError(ValueError):
    """Raised when an environment is not parsed correctly."""
    pass


class CannotExtractUtrData(HTTPError):
    """Exception raised when a request fails to extract Utr data."""
    pass
