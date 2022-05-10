from django.contrib import admin

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
# from django.utils.translation import gettext_lazy as _
from tinymce.widgets import TinyMCE
from django.db import models


# Define a new FlatPageAdmin
class CustomFlatPageAdmin(FlatPageAdmin):
    # fieldsets = (
    #     (None, {'fields': ('url', 'title', 'content', 'sites')}),
    #     (_('Advanced options'), {
    #         'classes': ('collapse',),
    #         'fields': (
    #             'enable_comments',
    #             'registration_required',
    #             'template_name',
    #         ),
    #     }),
    # )
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE}
    }


# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)