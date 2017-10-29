from logging import Logger
from typing import Iterable, Dict

from logomachy.logomachy_core import models as app_models


class DocumentsProcessor:
    """
    Documents Processor that takes many Documents and processes it to output
    to the database.
    """

    def __init__(self, logger: Logger):
        """
        Create a new documents processor.
        """

        self.logger = logger

    def run(self, documents: Iterable[app_models.Document]) -> Dict:
        """
        Run this processor. Use the data from `documents`.
        If the processing is successful, return a dict containing the data.
        If the processing fails, raise an exception.
        Make use of the logger.
        Do not touch the database in this method.
        """

        raise NotImplementedError("Provide an implementation of 'run'.")

    def run_db(self, documents: Iterable[app_models.Document]) -> None:
        """
        Run this processor. Use the data from `documents`.
        If the processing is successful, return.
        If the processing fails, raise an exception.
        Make use of the logger.
        Use the database in this method access existing data and save new data.
        """
        raise NotImplementedError("Provide an implementation of 'run_db'.")
