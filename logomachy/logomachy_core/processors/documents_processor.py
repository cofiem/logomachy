from logging import Logger
from typing import Iterable

from logomachy.logomachy_core import models as app_models


class DocumentsProcessor:
    """
    Documents Processor that takes a many Documents and processes it to output
    to the database.
    """

    def __init__(self, logger: Logger):
        """
        Create a new documents processor.
        """

        self.logger = logger

    def run(self, documents: Iterable[app_models.Document]) -> None:
        """
        Run this processor. Use the data from `documents`.
        See DocumentProcessor.run for more information.
        """

        raise NotImplementedError("Provide an implementation of 'run'.")
