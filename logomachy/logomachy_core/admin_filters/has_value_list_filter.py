from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class HasValueListFilter(admin.SimpleListFilter):
    """
    A list filter for easily filtering by whether a column has a value or not.
    """

    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = ''

    # Parameter for the filter that will be used in the URL query.
    parameter_name = ''

    # see https://stackoverflow.com/questions/7691890/filtering-django-admin-by-null-is-not-null

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('1', _('Has value')),
            ('0', _('No value')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        kwargs = {'{}__isnull'.format(self.parameter_name): True}
        if self.value() == '0':
            return queryset.filter(**kwargs)
        if self.value() == '1':
            return queryset.exclude(**kwargs)
        return queryset
