class TextInfo:

    def __init__(self, *args, **kwargs):
        self._values = {}
        if kwargs:
            for name, value in kwargs.items():
                if hasattr(self, name):
                    self._values[name] = value
                else:
                    raise ValueError('Invalid value for TextInfo {}:{}'.format(name, value))

    @property
    def character_count(self):
        return self._values.get('character_count')

    @property
    def word_count(self):
        return self._values.get('word_count')

    @property
    def sentence_count(self):
        return self._values.get('sentence_count')

    @property
    def syllable_count(self):
        return self._values.get('syllable_count')

    @property
    def polysyllable_count(self):
        return self._values.get('polysyllable_count')

    @property
    def syllable_count(self):
        return self._values.get('syllable_count')

    def word_letter_count(self, num_letters: int) -> int:
        raise NotImplementedError()
