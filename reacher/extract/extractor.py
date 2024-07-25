from classes import Utr


class UtrExtractor:
    """Extractor class for extracting UTR data"""

    def __init__(self, utr: Utr):
        self.utr = utr

    def extract(self, user_id: int) -> dict:
        """
        Extracts UTR data
        :return: Dictionary with extracted UTR data
        """
        profile = self.utr.get_profile(user_id)
        results = self.utr.get_results(user_id)
        return {
            'profile': profile,
            'results': results
        }
