from urllib import parse

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from logomachy.logomachy_core.admin_filters.has_value_list_filter import HasValueListFilter


def make_model_link(model_link_name: str, text: str, filter_conditions: dict = None):
    """
    Create a link to the admin list page for a model.
    filter_conditions is a dict where
    keys are the querystring keys (does not need to be escaped)
    values are the filtering text (which needs to be escaped)
    """

    search = ''

    if filter_conditions is not None:
        search = '?' + parse.urlencode(filter_conditions)

    url = reverse('admin:logomachy_core_{}_changelist'.format(model_link_name))
    return mark_safe('<a href="{}{}">{}</a>'.format(url, search, text))


def make_items_link(obj_association, model_admin_name, obj_id_association, obj_id):
    """
    Create a link to the admin list page for a model from an association.
    """

    if obj_association:
        obj_count = obj_association.count()
        if obj_count == 1:
            text = '{} item'.format(obj_count)
        else:
            text = '{} items'.format(obj_count)
        return make_model_link(model_admin_name, text, {obj_id_association: obj_id})
    else:
        return 'no items'


def custom_titled_filter(title):

    class AdminFilterWrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return AdminFilterWrapper


def custom_has_value_filter(field, filter_title=None):
    class CustomHasValueFieldFilter(HasValueListFilter):
        parameter_name = str(field)
        title = filter_title or field
    return CustomHasValueFieldFilter


class TimestampAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'modified_date')
    list_filter = ('created_date', 'modified_date')


class LookupListFilterAdmin(admin.ModelAdmin):
    # need to allow these lookups
    # see https://github.com/django/django/blob/9459ec82aa12cad9b859c54c2f33f50bec057f2e/django/contrib/auth/admin.py
    def lookup_allowed(self, lookup, value):
        if hasattr(self, 'lookup_list_filter') and lookup in self.lookup_list_filter:
            return True
        return super(admin.ModelAdmin, self).lookup_allowed(lookup, value)
