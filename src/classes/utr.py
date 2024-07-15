import posixpath

from requests import Session, HTTPError

from src.exceptions.exceptions import CannotExtractUtrData


class Utr(object):
    """A class to execute HTTP requests with a UTR server."""

    player = "player"
    api = "api"
    version = "v1"

    def __init__(self, url: str, username: str, password: str):
        """
        Initializes the UtrExtractor object.
        :param url: the base url of the UTR server
        :param username: a username for an account on the UTR server
        :param password: a password for an account on the UTR server
        """
        self.url = url
        session = Session()
        session.auth = (username, password)
        self.session = session

    def _get_wrapper(self, get_request_url: str, params: dict) -> dict:
        """
        Executes the GET request for the UTR server.
        :param get_request_url: the url to GET from the UTR server.
        :return: the GET response from the UTR server.
        """
        if params is None:
            params = {}
        response = self.session.get(get_request_url, params=params)
        response.raise_for_status()
        return response.json()

    def get_profile(self, user_id: int):
        """
        Gets profile data for a given user id.
        :param user_id: the user id to get profile data for
        :return: the profile data for the given user id
        """
        try:
            return self._get_wrapper(posixpath.join(self.url, self.api, self.version, self.player, str(user_id)), {})
        except HTTPError:
            raise CannotExtractUtrData(f"Unable to extract UTR profile data for user id: {user_id}")

    def get_results(self, user_id: int, year="last", match_type="singles"):
        """
        Gets results data for a given user id.
        :param user_id:  the user id to get results data for
        :param year: filter results by a certain year (e.g. 2024). Defaults to "last" to get latest results.
        :param match_type: the match type to filter results by (e.g. singles or doubles). Defaults to "singles".
        :return: the results data for the given user id
        """
        try:
            params = {
                "year": year,
                "type": match_type
            }
            return self._get_wrapper(
                posixpath.join(self.url, self.api, self.version, self.player, str(user_id), "results"),
                params=params
            )
        except HTTPError:
            raise CannotExtractUtrData(f"Unable to extract UTR results data for user id: {user_id}")
