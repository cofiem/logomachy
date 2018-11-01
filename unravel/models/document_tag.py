from django.db import models
from django.utils.text import slugify

from unravel import models as app_models


class DocumentTag(app_models.BaseModel):
    """A descriptive label assigned to zero, one, or more Documents."""

    title = models.CharField(
        max_length=300, null=False, blank=False, unique=True, help_text='Tag title')
    name = models.SlugField(
        max_length=100, null=False, blank=False, unique=True, help_text='Unique tag slug')
    description = models.TextField(
        null=True, blank=True, help_text='Tag description')
    documents = models.ManyToManyField(
        app_models.Document, related_name='tags', help_text='Documents assigned this tag')

    class Meta:
        verbose_name = 'Document Tag'
        verbose_name_plural = 'Document Tags'

    def __str__(self):
        return '{} Tag'.format(self.title)

    def save(self, *args, **kwargs):
        # if this is a new object, set the name / slug
        if not self.id:
            if self.name:
                self.name = slugify(self.name)
            else:
                self.name = slugify(self.title)

        super(DocumentTag, self).save(*args, **kwargs)
