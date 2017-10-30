from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class FleschKincaidGradeLevel(BaseReadability):
    """
    Presents a score as a U.S. grade level. It can also mean the number of years of education generally
    required to understand this text, relevant when the formula results in a number greater than 10.

    U.S. grade levels are 1 through 12.

    Description from https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests#Flesch.E2.80.93Kincaid_grade_level

    0.39 x (total words / total sentences) + 11.8 x (total syllables / total words) - 15.59
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        words = text_info.word_count
        sentences = text_info.sentence_count
        syllables = text_info.syllable_count

        if sentences < 1 or words < 1:
            return ReadingLevel.unknown

        result = 0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59
        level = ReadingLevel['grade_{}'.format(int(result))]
        return level
