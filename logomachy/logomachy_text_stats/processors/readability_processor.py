from typing import Iterable

from logomachy.logomachy_core.processors.documents_processor import DocumentsProcessor
from logomachy.logomachy_core import models as core_models


class ReadabilityProcessor(DocumentsProcessor):
    """
    A processor that calculates the readability of Documents.
    """

    # see
    # https://github.com/erinhengel/Textatistic
    # https://github.com/andreasvc/readability/
    # https://github.com/joaopalotti/readability_calculator
    # https://languagemachines.github.io/ucto/
    # https://github.com/mattselph/readability
    #
    # TODO: implement a number of algorithms for readability, and store the output in a db table
    def run(self, document: core_models.Document) -> None:
        pass

    def run_db(self, documents: Iterable[core_models.Document]) -> None:
        pass
