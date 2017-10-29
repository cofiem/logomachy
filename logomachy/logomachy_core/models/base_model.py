from logging import Logger
from typing import Dict, Tuple

from django.core import urlresolvers
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, FieldError, FieldDoesNotExist
from django.db import models
from django.db.models import Q
from django.db.models.constants import LOOKUP_SEP


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, help_text='The date the record was created.')
    modified_date = models.DateTimeField(auto_now=True, help_text='The date the record was last modified.')

    class Meta:
        abstract = True

    @classmethod
    def retrieve_or_create(cls, defaults: Dict = None, **kwargs) -> Tuple[models.Model, bool]:
        """
        Looks up an object with the given kwargs, building one if necessary.
        Returns a tuple of (object, created), where created is a boolean
        specifying whether an object was built. Does not save to db.
        Based on Django model method get_or_create.
        """

        lookup, params = cls._extract_model_params(cls, defaults, **kwargs)
        try:
            # if all the filters match exactly one item, then it was not created (created = false)
            return cls.objects.get(**lookup), False
        except cls.DoesNotExist:
            # otherwise create the item (created = true)
            # this might still fail when saving if e.g. unique constraint is not met
            params = {k: v() if callable(v) else v for k, v in params.items()}
            return cls(**params), True

    @classmethod
    def _extract_model_params(cls, model, defaults, **kwargs):
        """
        Prepares `lookup` (kwargs that are valid model attributes), `params`
        (for creating a model instance) based on given kwargs; for use by
        retrieve_or_create.
        Based on Django model method _extract_model_params.
        """

        defaults = defaults or {}
        lookup = kwargs.copy()
        for f in model._meta.fields:
            if f.attname in lookup:
                lookup[f.name] = lookup.pop(f.attname)
        params = {k: v for k, v in kwargs.items() if LOOKUP_SEP not in k}
        params.update(defaults)
        property_names = model._meta._property_names
        invalid_params = []
        for param in params:
            try:
                model._meta.get_field(param)
            except FieldDoesNotExist:
                # It's okay to use a model's property if it has a setter.
                if not (param in property_names and getattr(model, param).fset):
                    invalid_params.append(param)
        if invalid_params:
            raise FieldError(
                "Invalid field name(s) for model %s: '%s'." % (
                    model._meta.object_name,
                    "', '".join(sorted(invalid_params)),
                ))
        return lookup, params

    @classmethod
    def query_using_or(cls, **kwargs):
        """
        Construct an 'or' query using kwargs.
        """

        query = None
        for key, value in kwargs.items():
            if value:
                value_query = Q(**{key: value})
                if query is None:
                    query = value_query
                else:
                    query = (query | value_query)
        return query

    @classmethod
    def get_with_logging(cls, logger: Logger, *args, **kwargs):
        """
        Try to a single model instance from the db using args and kwargs.
        Logs ObjectDoesNotExist and MultipleObjectsReturned exceptions.
        """

        try:
            return cls.objects.get(*args, **kwargs)
        except ObjectDoesNotExist:
            logger.error("Nothing matched '{}' using '{}' and '{}'".format(cls.__name__, args, kwargs))
            raise
        except MultipleObjectsReturned:
            logger.error("More than one matching '{}' using '{}' and '{}'".format(cls.__name__, args, kwargs))
            raise

    @classmethod
    def get_admin_list_url(cls):
        """
        Get the url to an admin list page for a particular model in a particular application.
        """

        return urlresolvers.reverse("admin:{}_{}_change".format(cls._meta.app_label, cls._meta.model_name))
