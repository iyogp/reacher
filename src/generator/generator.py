from src.input.input_parser import InputParser

from src.classes.utr import Utr

from src.generator.extract.extractor import UtrExtractor


class UtrGenerator:

    def __init__(self):
        input_parser = InputParser()
        input_parser.parse_input()
        self.utr = Utr(
            url=input_parser.get_utr_url(),
            username=input_parser.get_utr_username(),
            password=input_parser.get_utr_password()
        )
        self.user_id = input_parser.get_utr_user_id()

    def extract(self):
        extractor = UtrExtractor(self.utr)
        data = extractor.extract(self.user_id)
        return data

    def generate(self):
        data = self.extract()
        # transform data
        # load data
        pass
