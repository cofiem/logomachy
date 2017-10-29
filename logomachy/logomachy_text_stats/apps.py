from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class LogomachyTextStatsConfig(AppConfig):
    """
    An application that defines various processors to calculate statistics over text documents.
    """

    name = 'logomachy.logomachy_text_stats'
    verbose_name = _('Logomachy: Text Stats')
