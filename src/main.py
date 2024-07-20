from dotenv import load_dotenv

from src.generator.generator import UtrGenerator


load_dotenv()


if __name__ == '__main__':

    generator = UtrGenerator()
    generator.generate()
