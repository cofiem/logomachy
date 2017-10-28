from django.db import models

from logomachy.logomachy_core.models import BaseModel, DocumentType


class Document(BaseModel):
    """A document containing text."""

    name = models.SlugField(
        max_length=100, unique=True, help_text='A unique, possibly generated, name for the document.')
    title = models.CharField(
        max_length=1000, help_text='The human-readable name of the document.')
    author = models.CharField(
        max_length=1000, help_text='The person, company, or other entity that created this document.')
    document_date = models.DateField(
        help_text='The date the document was retrieved or last updated.')
    source_url = models.URLField(
        max_length=2000, blank=True, null=True, help_text='The website this document was sourced from (optional).')
    document_version = models.CharField(
        max_length=100, blank=True, null=True, help_text='The version of this document (optional).')
    document_type = models.ForeignKey(
        DocumentType, on_delete=models.PROTECT, related_name='documents', help_text='The type of this document.')
    document_content = models.TextField(help_text='The content for this document.')
