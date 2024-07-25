from unittest import mock
from argparse import Namespace

from pytest import raises

from src.input.argument.argument_input_parser import ArgumentInputParser


class TestArgumentParser:

    @mock.patch('argparse.ArgumentParser.parse_args')
    def test_parse_arguments_with_user_id_value(self, mock_parse_args):
        mock_args = Namespace(user_id=12345)  # dest="user_id"
        mock_parse_args.return_value = mock_args
        parser = ArgumentInputParser()
        parser.parse_arguments()
        user_id = parser.get_user_id()
        assert user_id == 12345

    def test_parse_arguments_without_user_id_value(self):
        with raises(SystemExit) as exc_info:
            parser = ArgumentInputParser()
            parser.parse_arguments()
        # https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.error
        assert exc_info.value.code == 2
