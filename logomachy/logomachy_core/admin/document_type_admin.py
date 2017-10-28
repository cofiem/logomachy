from logomachy.logomachy_core.admin.common_admin import TimestampAdmin, LookupListFilterAdmin


class DocumentTypeAdmin(TimestampAdmin, LookupListFilterAdmin):
    list_display = ('name', 'description') + TimestampAdmin.list_display
    list_filter = TimestampAdmin.list_filter + ()
    lookup_list_filter = ()
    list_per_page = 30
