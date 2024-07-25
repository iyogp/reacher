from input import InputParser
from classes import Utr
from extract import UtrExtractor


class UtrGenerator:

    def __init__(self):
        input_parser = InputParser()
        input_parser.parse_input()
        self.utr = Utr(
            url=input_parser.get_url(),
            username=input_parser.get_username(),
            password=input_parser.get_password()
        )
        self.user_id = input_parser.get_user_id()

    def extract(self):
        extractor = UtrExtractor(self.utr)
        data = extractor.extract(self.user_id)
        return data

    def generate(self):
        data = self.extract()
        # transform data
        # load data
        pass
