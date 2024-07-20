from unittest import mock
from argparse import Namespace

from src.input.argument.argument_input_parser import ArgumentInputParser


class TestArgumentParser:

    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args):
        # simulate command line arguments
        mock_args = Namespace(user_id=12345)  # dest="user_id"
        mock_parse_args.return_value = mock_args
        parser = ArgumentInputParser()
        parser.parse_arguments()
        user_id = parser.get_user_id()
        assert user_id == 12345
