from requests import HTTPError


class CannotExtractUtrData(HTTPError):
    """Exception raised when a request fails to extract Utr data."""
    pass
