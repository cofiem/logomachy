from io import TextIOBase

from logomachy.logomachy_core.text_analyser.text_info import TextInfo


class BaseTextAnalyser:
    def get_text_info(self, text: str) -> TextInfo:
        raise NotImplementedError()

    def get_text_info_stream(self, text_stream: TextIOBase) -> TextInfo:
        raise NotImplementedError()
