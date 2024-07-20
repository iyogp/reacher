from argparse import ArgumentParser

from src.exceptions.exceptions import ArgumentInputNotParsedError


class ArgumentParser:
    """Parses command line arguments"""

    def __init__(self):
        self.parser = ArgumentParser()
        self.args = None

    def _parse_utr_user_id(self, parser: ArgumentParser):
        """
        Parses the UTR user id
        :param parser: ArgumentParser object to parse the UTR user id
        """
        parser.add_argument(
            "-u"
            "--uid",
            dest="user_id",
            action="store",
            help="The id for the UTR user account",
            required=True
        )

    def parse_arguments(self):
        """Parses the arguments"""
        parser = self.parser
        self._parse_utr_user_id(parser)
        self.args = parser.parse_args()

    def get_utr_user_id(self):
        """
        Gets the UTR user id from the arguments
        :return: the UTR user id
        """
        if self.args is None:
            raise ArgumentInputNotParsedError("Arguments not parsed")
        else:
            return self.args.user_id
