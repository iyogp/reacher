import os

from src.constants import UTR_URL, UTR_USERNAME, UTR_PASSWORD

from src.exceptions.exceptions import EnvironmentInputNotParsedError


class EnvironmentParser:
    """Parsers environment variables"""

    def __init__(self):
        self.url = None
        self.username = None
        self.password = None

    def parse_url(self):
        """Parse the URL provided from the environment"""
        self.url = os.getenv(UTR_URL)

    def parse_username(self):
        """Parse the username provided from the environment"""
        self.username = os.getenv(UTR_USERNAME)

    def parse_password(self):
        """Parse the password provided from the environment"""
        self.password = os.getenv(UTR_PASSWORD)

    def parse_environment(self):
        """Parses the environment variables"""
        self.parse_url()
        self.parse_username()
        self.parse_password()

    def get_utr_url(self):
        """
        Get the UTR url from the environment
        :return: the UTR url
        """
        if self.url is None:
            raise EnvironmentInputNotParsedError(f"{UTR_URL} has not been set or parsed")
        else:
            return self.url

    def get_username(self):
        """
        Get the username from the environment
        :return: the username from the environment
        """
        if self.username is None:
            raise EnvironmentInputNotParsedError(f"{UTR_USERNAME} has not been set or parsed")
        else:
            return self.username

    def get_password(self):
        """
        Get the password from the environment
        :return: the password from the environment
        """
        if self.password is None:
            raise EnvironmentInputNotParsedError(f"{UTR_PASSWORD} has not been set or parsed")
        else:
            return self.password
