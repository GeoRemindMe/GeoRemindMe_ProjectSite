from django.contrib import admin

from geostatic import models

class Page(admin.ModelAdmin):
    model = models.Page
    
    list_display = ('subdomain','slug','template',)

admin.site.register(models.Page,Page)
