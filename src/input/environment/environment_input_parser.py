import os

from constants import UTR_URL, UTR_USERNAME, UTR_PASSWORD
from exceptions import EnvironmentInputNotParsedError


class EnvironmentInputParser:
    """Parsers environment variables"""

    def __init__(self):
        self.url = None
        self.username = None
        self.password = None

    def parse_required(self, key: str):
        value = os.getenv(key)
        if value is None:
            raise EnvironmentInputNotParsedError(f"Environment variable \"{key}\" has not been set or parsed")
        else:
            return value

    def parse_environment(self):
        """Parses the environment variables"""
        self.url = self.parse_required(UTR_URL)
        self.username = self.parse_required(UTR_USERNAME)
        self.password = self.parse_required(UTR_PASSWORD)

    def get_url(self):
        """
        Get the UTR url from the environment
        :return: the UTR url
        """
        return self.url

    def get_username(self):
        """
        Get the username from the environment
        :return: the username from the environment
        """
        return self.username

    def get_password(self):
        """
        Get the password from the environment
        :return: the password from the environment
        """
        return self.password
