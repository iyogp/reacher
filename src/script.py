from dotenv import load_dotenv

from generator import UtrGenerator


load_dotenv()


def main():
    utr_generator = UtrGenerator()
    utr_generator.generate()


if __name__ == '__main__':
    main()
