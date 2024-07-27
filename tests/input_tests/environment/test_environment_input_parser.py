import os

import pytest

from reacher import UTR_URL, UTR_USERNAME, UTR_PASSWORD
from reacher import EnvironmentInputParser, EnvironmentInputNotParsedError


class TestEnvironmentInputParser:

    TEST_UTR_URL = "www.someurl.com"
    TEST_UTR_USERNAME = "aUsername"
    TEST_UTR_PASSWORD = "aPassword"

    def test_parse_required(self):
        fake_key = "FAKE_KEY"
        with pytest.raises(EnvironmentInputNotParsedError) as exc_info:
            parser = EnvironmentInputParser()
            parser.parse_required(fake_key)
        assert str(exc_info.value) == f"Environment variable \"{fake_key}\" has not been set or parsed"

    @pytest.fixture
    def mock_environment(self, monkeypatch):
        monkeypatch.setenv(UTR_URL, self.TEST_UTR_URL)
        monkeypatch.setenv(UTR_USERNAME, self.TEST_UTR_USERNAME)
        monkeypatch.setenv(UTR_PASSWORD, self.TEST_UTR_PASSWORD)

    def test_parse_environment(self, mock_environment):
        lol = os.environ
        parser = EnvironmentInputParser()
        parser.parse_environment()
        assert parser.get_url() == self.TEST_UTR_URL
        assert parser.get_username() == self.TEST_UTR_USERNAME
        assert parser.get_password() == self.TEST_UTR_PASSWORD
