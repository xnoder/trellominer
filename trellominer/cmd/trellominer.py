import argparse
import sys

import requests

from trellominer.api import trello
from trellominer.processor import excel


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help="Show version number and exit.")
    args = parser.parse_args()

    boards = trello.Trello().boards()
    # Turn boards into worksheets in a workbook
    excel.Excel().process_boards(boards)


if __name__ == "__main__":
    main()
