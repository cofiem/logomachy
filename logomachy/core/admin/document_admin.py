from logomachy.core.admin.common_admin import TimestampAdmin, LookupListFilterAdmin


class DocumentAdmin(TimestampAdmin, LookupListFilterAdmin):
    # list_display = TimestampAdmin.list_display + ()
    # list_filter = TimestampAdmin.list_filter + ()
    lookup_list_filter = ()
    list_per_page = 30
    prepopulated_fields = {'name': ("title",)}
