from django.contrib import admin

from . import models


class RezepteAdmin(admin.ModelAdmin):
    pass
    # inlines = [KategorieInLine]


admin.site.register(models.Rezept, RezepteAdmin)
admin.site.register(models.Kategorie)
admin.site.register(models.Favorite)
