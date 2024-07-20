from src.input.argument.argument_parser import ArgumentParser
from src.input.environment.environment_parser import EnvironmentParser


class Input:
    """Parsers input arguments and environment variables"""

    def __init__(self):
        self.argument_parser = ArgumentParser()
        self.environment_parser = EnvironmentParser()

    def parse_input(self):
        """Parsers the inputs from command line arguments and the environment"""
        self.argument_parser.parse_arguments()
        self.environment_parser.parse_environment()

    def get_utr_user_id(self):
        """
        Get the UTR user ID from the command line arguments
        :return: the UTR user ID
        """
        return self.argument_parser.get_utr_user_id()

    def get_utr_url(self):
        """
        Get the UTR URL from the environment variables
        :return: the UTR URL
        """
        return self.environment_parser.get_utr_url()

    def get_utr_username(self):
        """
        Get the UTR username from the environment variables
        :return: the UTR username
        """
        return self.environment_parser.get_username()

    def get_utr_password(self):
        """
        Get the UTR password from the environment variables
        :return: the UTR password
        """
        return self.environment_parser.get_password()
