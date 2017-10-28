from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from logomachy.logomachy_auth import models as auth_models
from logomachy.logomachy_core import models as core_models
from logomachy.logomachy_core.admin.document_admin import DocumentAdmin
from logomachy.logomachy_core.admin.document_type_admin import DocumentTypeAdmin


class LogomachyAdminSite(AdminSite):
    site_header = _('Logomachy administration')
    site_title = _('Logomachy site admin')
    index_title = _('Logomachy site administration')


admin_site = LogomachyAdminSite(name='logomachy_admin')

admin_site.register(core_models.DocumentType, DocumentTypeAdmin)
admin_site.register(core_models.Document, DocumentAdmin)

admin_site.register(Group, GroupAdmin)

# for custom user, see https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#extending-user
admin_site.register(auth_models.User, UserAdmin)
