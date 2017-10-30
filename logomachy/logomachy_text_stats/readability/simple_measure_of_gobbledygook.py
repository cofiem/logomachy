from math import sqrt

from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class SimpleMeasureOfGobbledygook(BaseReadability):
    """
    The SMOG grade is a measure of readability that estimates the years of education needed to understand a
    piece of writing. It gives the estimates grade required to fully SMOG is an acronym for Simple Measure of Gobbledygook.
    SMOG is widely used, particularly for checking health messages.

    Description from https://en.wikipedia.org/wiki/SMOG

    0.4 x ((total words / total sentences) + 100 * (total complex words / total words))
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        sentences = text_info.sentence_count
        polysyllable_words = text_info.polysyllable_word_count

        if sentences < 1:
            return ReadingLevel.unknown

        if sentences < 30:
            self._logger.warning('Calculating SMOG readability on text with fewer '
                                 'than 30 sentences ({})'.format(sentences))

        result = 1.0430 * sqrt(polysyllable_words * 30.0 / sentences) + 3.1291
        level = ReadingLevel['grade_{}'.format(int(result))]
        return level
