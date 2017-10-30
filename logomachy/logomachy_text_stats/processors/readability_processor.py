from typing import Iterable

from logomachy.logomachy_core.processors.documents_processor import DocumentsProcessor
from logomachy.logomachy_core import models as core_models


class ReadabilityProcessor(DocumentsProcessor):
    """
    A processor that calculates the readability of Documents.
    """

    def run(self, document: core_models.Document) -> None:
        pass

    def run_db(self, documents: Iterable[core_models.Document]) -> None:
        pass
