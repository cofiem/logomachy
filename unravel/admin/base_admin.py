from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        # need to include the current user when saving the model
        # SEE ALSO: super().save_model(request, obj, form, change)
        obj.save(request=request)

    def delete_model(self, request, obj):
        # need to include the current user when saving the model
        # SEE ALSO: super().delete_model(request, obj)
        obj.delete(request=request)
