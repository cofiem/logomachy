from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class LogomachyCoreConfig(AppConfig):
    """
    An application that defines the essential elements of Logomachy.
    """

    name = 'logomachy.logomachy_core'
    verbose_name = _('Logomachy: Core')
