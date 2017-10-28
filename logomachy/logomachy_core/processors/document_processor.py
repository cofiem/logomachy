from logging import Logger

from logomachy.logomachy_core import models as app_models


class DocumentProcessor:
    """
    Document Processor that takes a single Document and processes it to output
    to the database.
    """

    def __init__(self, logger: Logger):
        """
        Create a new document processor.
        """

        self.logger = logger

    def run(self, document: app_models.Document) -> None:
        """
        Run this processor. Use the data from `document`.
        If the processing is successful, simply exit.
        If the processing fails, raise an exception.
        Make use of the Django database API for your application to save processed data.
        Make use of the logger.
        """

        raise NotImplementedError("Provide an implementation of 'run'.")
