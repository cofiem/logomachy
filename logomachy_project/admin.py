from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group, User

from logomachy.core import models as core_models


class LogomachyAdminSite(AdminSite):
    site_header = 'Logomachy administration'
    site_title = 'Logomachy site admin'
    index_title = 'Logomachy site administration'


admin_site = LogomachyAdminSite(name='logomachy_admin')

admin_site.register(core_models.DocumentType)
admin_site.register(core_models.Document)

admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
