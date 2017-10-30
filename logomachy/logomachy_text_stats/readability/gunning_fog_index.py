from logomachy.logomachy_text_stats.readability.base_readability import BaseReadability, ReadingLevel


class GunningFogIndex(BaseReadability):
    """
    The index estimates the years of formal education a person needs to understand the text on the first reading.
    A fog index of 12 requires the reading level of a U.S. high school senior (around 18 years old).
    Texts for a wide audience generally need a fog index less than 12.
    Texts requiring near-universal understanding generally need an index less than 8.

    Fog Index    Reading level by grade
        17          College graduate
        16          College senior
        15          College junior
        14          College sophomore
        13          College freshman
        12          High school senior
        11          High school junior
        10          High school sophomore
        9           High school freshman
        8           Eighth grade
        7           Seventh grade
        6           Sixth grade

    Description from https://en.wikipedia.org/wiki/Gunning_fog_index

    0.4 x ((total words / total sentences) + 100 * (total complex words / total words))
    """

    def calc(self, text: str) -> ReadingLevel:
        if not text:
            return ReadingLevel.unknown
        text_info = self._text_analyser.get_text_info(text)
        words = text_info.word_count
        sentences = text_info.sentence_count
        polysyllable_words = text_info.polysyllable_count

        if sentences < 1 or words < 1:
            return ReadingLevel.unknown

        result = 0.4 * ((words / sentences) + 100.0 * (polysyllable_words / words))
        level = ReadingLevel['grade_{}'.format(int(result))]
        return level
