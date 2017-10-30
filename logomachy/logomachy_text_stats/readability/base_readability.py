from enum import Enum, unique
from logging import Logger


class BaseReadability:
    def __init__(self, logger: Logger, text_analyser):
        self._logger = logger
        self._text_analyser = text_analyser

    def calc(self, text: str) -> ReadingLevel:
        """
        Calculate the readability metric on text.
        Return an estimate of the number of years of
        education required to understand the text.
        """

        raise NotImplementedError()


@unique
class ReadingLevel(Enum):
    """
    An enum indicating U.S. grade level and/or average minimum age
    required to understand a text.
    """

    unknown = 0

    # primary
    grade_1 = 5
    grade_2 = 6
    grade_3 = 7
    grade_4 = 8

    # middle
    grade_5 = 9
    grade_6 = 10
    grade_7 = 11
    grade_8 = 12

    # high
    grade_9 = 13
    grade_10 = 14
    grade_11 = 15
    grade_12 = 16

    # tertiary
    grade_13 = 17
    grade_14 = 18
    grade_15 = 19
    grade_16 = 20
    grade_17 = 21
