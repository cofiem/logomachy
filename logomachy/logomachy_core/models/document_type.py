from django.db import models
from logomachy.logomachy_core.models import BaseModel


class DocumentType(BaseModel):
    """
    The possible types of documents.
    """

    name = models.SlugField(max_length=100, unique=True, help_text='The name of the document type.')
    description = models.CharField(max_length=2000, help_text='The description of the document type.')
