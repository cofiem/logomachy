from django.utils.translation import ugettext_lazy as _

from django.apps import AppConfig


class LogomachyAuthConfig(AppConfig):
    """
    An application that defines custom authorisation for Logomachy.
    """

    name = 'logomachy.logomachy_auth'
    verbose_name = _('Logomachy: Auth')
