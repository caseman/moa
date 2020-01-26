"""Launch a new game"""
import argparse
from .game import Game


def main():
    parser = argparse.ArgumentParser(
        'masterofascii',
        description='A space conquest game in an ASCII universe')
    parser.add_argument('--debug',
                        action='store_true',
                        help='debug level output')
    args = parser.parse_args()

    Game(args).run()


if __name__ == '__main__':
    main()
