from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class Lix(BaseReadability):
    """
    LIX is a readability measure indicating the difficulty of reading a text.
    Long words contain more than 6 letters i.e. long words contain 7 or more letters.

    LIX score      Grade Level
     56+            College
     52-55          12
     48-51          11
     44-47          10
     40-43          9
     36-39          8
     32-35          7
     28-31          6
     24-27          5
     20-23          4
     15-19          3
     10-14          2
     Below 10       1

    Conversion table from Lix and Rix: Variations on a Little-known Readability Index, Anderson, J.,
    Vol. 26, No. 6 (Mar., 1983), pp. 490-496, http://www.jstor.org/stable/40031755

    Description from http://www.readabilityformulas.com/the-LIX-readability-formula.php

    (total words / total periods) + ((number of long words * 100) / total words)
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        words = text_info.word_count
        long_words = text_info.word_letter_count(7)
        sentences = text_info.sentence_count

        if sentences < 1 or words < 1:
            return ReadingLevel.unknown

        result = (words / sentences) + ((long_words * 100.0) / words)
        if result < 10:
            level = ReadingLevel.grade_1
        elif result < 15:
            level = ReadingLevel.grade_2
        elif result < 20:
            level = ReadingLevel.grade_3
        elif result < 24:
            level = ReadingLevel.grade_4
        elif result < 28:
            level = ReadingLevel.grade_5
        elif result < 32:
            level = ReadingLevel.grade_6
        elif result < 36:
            level = ReadingLevel.grade_7
        elif result < 40:
            level = ReadingLevel.grade_8
        elif result < 44:
            level = ReadingLevel.grade_9
        elif result < 48:
            level = ReadingLevel.grade_10
        elif result < 52:
            level = ReadingLevel.grade_11
        elif result < 56:
            level = ReadingLevel.grade_12
        elif result < 60:  # this is made up
            level = ReadingLevel.grade_13
        elif result < 64:  # this is made up
            level = ReadingLevel.grade_14
        elif result < 68:  # this is made up
            level = ReadingLevel.grade_15
        elif result < 72:  # this is made up
            level = ReadingLevel.grade_16
        else:  # this is made up
            level = ReadingLevel.grade_17
        return level
