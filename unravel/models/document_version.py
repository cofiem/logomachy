from django.contrib.postgres import search
from django.db import models

from unravel import models as app_models


class DocumentVersion(app_models.BaseModel):
    """A Document version."""

    CONTENT_TEXT_LANGUAGES = (
        ('english', 'English Language'),
        ('danish', 'Danish Language'),
        ('dutch', 'Dutch Language'),
        ('finnish', 'Finnish Language'),
        ('french', 'French Language'),
        ('german', 'German Language'),
        ('hungarian', 'Hungarian Language'),
        ('italian', 'Italian Language'),
        ('norwegian', 'Norwegian Language'),
        ('portuguese', 'Portuguese Language'),
        ('romanian', 'Romanian Language'),
        ('russian', 'Russian Language'),
        ('spanish', 'Spanish Language'),
        ('swedish', 'Swedish Language'),
        ('turkish', 'Turkish Language'),
        ('simple', 'Unspecified Language'),
    )

    last_authored_date = models.DateTimeField(
        blank=True, null=True, help_text='Date this version of the document was most recently edited.')
    content_language = models.CharField(
        max_length=20, null=False, blank=False, default='english', choices=CONTENT_TEXT_LANGUAGES,
        help_text='The language of the document text.')

    content_file = models.FileField(
        null=True, blank=True, upload_to='document/%Y/%m/%d/', max_length=200,
        help_text='The file containing the document content.')
    content_text_raw = models.TextField(
        null=True, blank=True, help_text='The raw document text.')
    content_text_formatted = models.TextField(
        null=True, blank=True, help_text='The formatted document text.')

    # the norm and simple content text are PostgreSQL tsvector, they are set by celery tasks
    content_text_norm = search.SearchVectorField(
        blank=True, null=True, editable=False, help_text='The document text normalised using the specified language.')
    content_text_simple = search.SearchVectorField(
        blank=True, null=True, editable=False, help_text='The document text normalised using a simpler method.')

    document = models.ForeignKey(
        app_models.Document, on_delete=models.CASCADE, related_name='versions',
        help_text='Metadata for the document that does not change between versions.')

    class Meta:
        verbose_name = 'Document Version'
        verbose_name_plural = 'Document Versions'

    def __str__(self):
        return '{} ({})'.format(self.document.title, self.last_authored_date)
