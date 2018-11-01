from django.conf import settings
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.db import models


class BaseModel(models.Model):
    """An abstract base model that provides common attributes and behaviour."""

    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_created', related_query_name='%(app_label)s_%(class)s_creators')

    updated_date = models.DateTimeField(auto_now=True)
    updated_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_updated', related_query_name='%(app_label)s_%(class)s_updaters')

    archived_date = models.DateTimeField(blank=True, null=True)
    archived_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='%(app_label)s_%(class)s_archived', related_query_name='%(app_label)s_%(class)s_archivers')

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # add LogEntry log_action
        request = self._get_request_user(**kwargs)
        if self.pk is None:
            # add / create
            msg = [{'added': {
                'name': str(self._meta.verbose_name),
                'object': str(self),
            }}]
            self._log_addition(request, self, msg)
            self.created_user = request.user
        else:
            # update / modify - fields: list of field names
            msg = [{'added': {
                'name': str(self._meta.verbose_name),
                'object': str(self),
                'fields': sorted(f.name for f in self._meta.get_fields()),
            }}]
            self._log_change(request, self, msg)
            self.updated_user = request.user

        # save object
        if 'request' in kwargs:
            kwargs.pop('request')
        super(BaseModel, self).save(*args, **kwargs)

        # TODO: include user in save

    def delete(self, *args, **kwargs):
        # add LogEntry log_action
        request = self._get_request_user(**kwargs)
        self._log_deletion(request, self, str(self))
        self.archived_user = request.user

        # delete object
        if 'request' in kwargs:
            kwargs.pop('request')
        return super(BaseModel, self).delete(*args, **kwargs)

    def _get_request_user(self, **kwargs):
        request = kwargs.get('request')
        if not request or not request.user or request.user.is_anonymous:
            raise ValueError(
                'Must pass request with valid logged in user for creating, updating, or deleting a model instance.')
        return request

    def _log_addition(self, request, obj, message):
        """
        Log that an object has been successfully added.

        Creates an admin LogEntry object.
        """
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=ADDITION,
            change_message=message,
        )

    def _log_change(self, request, obj, message):
        """
        Log that an object has been successfully changed.

        Creates an admin LogEntry object.
        """
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=str(obj),
            action_flag=CHANGE,
            change_message=message,
        )

    def _log_deletion(self, request, obj, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        Creates an admin LogEntry object.
        """
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=ContentType.objects.get_for_model(obj, for_concrete_model=False).pk,
            object_id=obj.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )
