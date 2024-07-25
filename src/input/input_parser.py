from src.input.argument.argument_input_parser import ArgumentInputParser
from src.input.environment.environment_input_parser import EnvironmentInputParser


class InputParser:
    """Parsers input arguments and environment variables"""

    def __init__(self):
        self.argument_parser = ArgumentInputParser()
        self.environment_parser = EnvironmentInputParser()

    def parse_input(self):
        """Parsers the inputs from command line arguments and the environment"""
        self.argument_parser.parse_arguments()
        self.environment_parser.parse_environment()

    def get_user_id(self):
        """
        Get the UTR user ID from the command line arguments
        :return: the UTR user ID
        """
        return self.argument_parser.get_user_id()

    def get_url(self):
        """
        Get the UTR URL from the environment variables
        :return: the UTR URL
        """
        return self.environment_parser.get_url()

    def get_username(self):
        """
        Get the UTR username from the environment variables
        :return: the UTR username
        """
        return self.environment_parser.get_username()

    def get_password(self):
        """
        Get the UTR password from the environment variables
        :return: the UTR password
        """
        return self.environment_parser.get_password()
