from django.db import models
from logomachy.core.models import BaseModel


class DocumentType(BaseModel):
    """
    The possible types of documents.
    """

    name = models.CharField(max_length=100, help_text='The name of the document type.')
    description = models.CharField(max_length=2000, help_text='The description of the document type.')
