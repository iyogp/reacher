import pytest

from src.input.environment.environment_input_parser import EnvironmentInputParser

from src.exceptions.exceptions import EnvironmentInputNotParsedError


class TestEnvironmentInputParser:

    def test_parse_required(self):
        fake_key = "FAKE_KEY"
        with pytest.raises(EnvironmentInputNotParsedError) as exc_info:
            parser = EnvironmentInputParser()
            parser.parse_required(fake_key)
        assert str(exc_info.value) == f"Environment variable \"{fake_key}\" has not been set or parsed"

    def test_parse_environment(self):
        parser = EnvironmentInputParser()
        parser.parse_environment()
        assert parser.get_url() == "www.someurl.com"
        assert parser.get_username() == "someUsername"
        assert parser.get_password() == "somePassword"
