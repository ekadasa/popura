from django.contrib import admin

from .models import Url, UrlView, UrlViewMeta

@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('slug', 'url')

admin.site.register(UrlView)
admin.site.register(UrlViewMeta)
