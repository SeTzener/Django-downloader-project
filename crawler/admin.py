from django.contrib import admin
from .models import RootUrl, ItemUrl

class RootUrlAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'root_url']}),
        ('Date information', {'fields': ['start_date', 'stop_date', 'last_update_date']}),
        ]
    list_display = ('name', 'start_date', 'stop_date', 'last_update_date')

class ItemUrlAdmin(admin.ModelAdmin):
    list_display = ('item_url', 'item_content', 'acquired_date')

admin.site.register(RootUrl, RootUrlAdmin)
admin.site.register(ItemUrl)
