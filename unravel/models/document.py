from django.db import models

from unravel import models as app_models


class Document(app_models.BaseModel):
    """A Company's policy or legal form."""

    title = models.CharField(
        max_length=300, null=False, blank=False, unique=True, help_text='Document title.')
    description = models.CharField(
        max_length=1000, null=True, blank=True, help_text='Summary of document content.')

    # FKs: results, versions
    # M2Ms: tags

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
