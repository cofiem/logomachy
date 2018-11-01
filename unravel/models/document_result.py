from django.db import models

from unravel import models as app_models


class DocumentResult(app_models.BaseModel):
    """Output from analysing one or more Documents."""

    documents = models.ManyToManyField(
        app_models.Document, related_name='results', help_text='Documents that were analysed.')

    class Meta:
        verbose_name = 'Document Result'
        verbose_name_plural = 'Document Results'

    def __str__(self):
        return 'Results for {} documents'.format(self.documents.count())
