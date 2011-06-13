from django.contrib import admin

from geostatic import models

class Page(admin.ModelAdmin):
    model = models.Page

admin.site.register(models.Page,Page)
