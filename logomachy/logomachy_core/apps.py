from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class LogomachyCoreConfig(AppConfig):
    name = 'logomachy.logomachy_core'
    verbose_name = _('Logomachy: Core')
