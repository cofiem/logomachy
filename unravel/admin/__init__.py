from .document_admin import DocumentAdmin
from .document_result_admin import DocumentResultAdmin
from .document_tag_admin import DocumentTagAdmin
from .document_version_admin import DocumentVersionAdmin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from unravel import models as app_models

admin.site.register(app_models.User, UserAdmin)

admin.site.register(app_models.Document, DocumentAdmin)
admin.site.register(app_models.DocumentResult, DocumentResultAdmin)
admin.site.register(app_models.DocumentTag, DocumentTagAdmin)
admin.site.register(app_models.DocumentVersion, DocumentVersionAdmin)
