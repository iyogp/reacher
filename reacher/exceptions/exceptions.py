from requests import HTTPError


class EnvironmentInputNotParsedError(ValueError):
    """Raised when an environment is not parsed correctly."""
    pass


class CannotExtractUtrData(HTTPError):
    """Exception raised when a request fails to extract Utr data."""
    pass
