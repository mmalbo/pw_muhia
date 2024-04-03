from django.contrib import admin
from .models import Curio, Event

class CurioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class EventAdmin(admin.ModelAdmin):
    pass

admin.site.register(Curio, CurioAdmin)
admin.site.register(Event, EventAdmin)