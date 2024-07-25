from argparse import ArgumentParser


class ArgumentInputParser:
    """Parses command line arguments"""

    def __init__(self):
        self.parser = ArgumentParser()
        self.args = None

    def add_arguments(self):
        """
        Add arguments from command line
        :param parser: ArgumentParser object to parse
        """
        # add argument for UTR user id
        self.parser.add_argument(
            "-u",
            dest="user_id",
            action="store",
            help="The id for the UTR user account",
            required=True,
            type=int
        )

    def parse_arguments(self):
        """Parses the arguments"""
        self.add_arguments()
        self.args = self.parser.parse_args()

    def get_user_id(self):
        """
        Gets the UTR user id from the arguments
        :return: the UTR user id
        """
        return self.args.user_id
