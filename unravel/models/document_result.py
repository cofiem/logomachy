from django.db import models

from unravel import models as app_models


class DocumentResult(app_models.BaseModel):
    """Output from analysing a document."""

    document = models.ForeignKey(
        app_models.Document, on_delete=models.CASCADE, related_name='results', help_text='Document that was analysed.')

    class Meta:
        verbose_name = 'Document Result'
        verbose_name_plural = 'Document Results'

    def __str__(self):
        return 'Results for {}'.format(self.document.title)
