from django.db import models

from unravel import models as app_models


class Document(app_models.BaseModel):
    """A company, government, or other entity's law, policy, or legal form.
    Use tags to identify the company, product, or purpose of the Document."""

    title = models.CharField(
        max_length=300, null=False, blank=False, unique=True, help_text='Document title.')
    description = models.CharField(
        max_length=1000, null=True, blank=True, help_text='Summary of document content.')

    # FKs: versions
    # M2Ms: tags, results

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title
