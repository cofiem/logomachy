from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class Rix(BaseReadability):
    """
    A simpler version of LIX. Uses words of 7 or more chars as long words.

    Rix score       grade level
    7.2+              College
    6.2+                12
    5.3+                11
    4.5+                10
    3.7+                9
    3.0+                8
    2.4+                7
    1.8+                6
    1.3+                5
    0.8+                4
    0.5+                3
    0.2+                2
    <0.2                1

    Information from Conversion table from Lix and Rix: Variations on a Little-known Readability Index, Anderson, J.,
    Vol. 26, No. 6 (Mar., 1983), pp. 490-496, http://www.jstor.org/stable/40031755

    number of long words / total sentences
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        long_words = text_info.word_letter_count(7)
        sentences = text_info.sentence_count

        if sentences < 1:
            return ReadingLevel.unknown

        result = long_words / sentences
        if result < 0.2:
            level = ReadingLevel.grade_1
        elif result < 0.5:
            level = ReadingLevel.grade_2
        elif result < 0.8:
            level = ReadingLevel.grade_3
        elif result < 1.3:
            level = ReadingLevel.grade_4
        elif result < 1.8:
            level = ReadingLevel.grade_5
        elif result < 2.4:
            level = ReadingLevel.grade_6
        elif result < 3.0:
            level = ReadingLevel.grade_7
        elif result < 3.7:
            level = ReadingLevel.grade_8
        elif result < 4.5:
            level = ReadingLevel.grade_9
        elif result < 5.3:
            level = ReadingLevel.grade_10
        elif result < 6.2:
            level = ReadingLevel.grade_11
        elif result < 7.2:
            level = ReadingLevel.grade_12
        elif result < 8.3:  # this is made up
            level = ReadingLevel.grade_13
        elif result < 9.5:  # this is made up
            level = ReadingLevel.grade_14
        elif result < 10.8:  # this is made up
            level = ReadingLevel.grade_15
        elif result < 12.2:  # this is made up
            level = ReadingLevel.grade_16
        else:  # this is made up
            level = ReadingLevel.grade_17
        return level
