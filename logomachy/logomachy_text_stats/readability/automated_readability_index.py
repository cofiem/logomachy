from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class AutomatedReadabilityIndex(BaseReadability):
    """
    Produces an approximate representation of the US grade level needed to comprehend the text.

    Description from https://en.wikipedia.org/wiki/Automated_readability_index

    4.71 x (total characters / total words) + 0.5 x (total words / total sentences) - 21.43
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        characters = text_info.character_count
        words = text_info.word_count
        sentences = text_info.sentence_count

        if words < 1 or sentences < 1:
            return ReadingLevel.unknown

        result = 4.71 * (characters / words) + 0.5 * (words / sentences) - 21.43
        level = ReadingLevel['grade_{}'.format(int(result))]
        return level
