from argparse import ArgumentParser


class ArgumentInputParser:
    """Parses command line arguments"""

    def __init__(self):
        self.args = None

    def add_arguments(self, parser: ArgumentParser):
        """
        Add arguments from command line
        :param parser: ArgumentParser object to parse
        """
        # add argument for UTR user id
        parser.add_argument(
            "-u"
            "--uid",
            dest="user_id",
            action="store",
            help="The id for the UTR user account",
            required=True,
            type=int
        )

    def parse_arguments(self):
        """Parses the arguments"""
        parser = ArgumentParser()
        self.add_arguments(parser)
        self.args = parser.parse_args()

    def get_utr_user_id(self):
        """
        Gets the UTR user id from the arguments
        :return: the UTR user id
        """
        return self.args.user_id
