from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class LogomachyTextStatsConfig(AppConfig):
    name = 'logomachy.logomachy_text_stats'
    verbose_name = _('Logomachy: Text Stats')
