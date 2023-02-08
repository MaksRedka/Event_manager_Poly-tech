from django.contrib import admin
from .models import Event, EventType
# Register your models here.

class EventModelAdmin(admin.ModelAdmin):
     list_filter = [
         "event_type",
         "timestamp"
    ]

admin.site.register(Event, EventModelAdmin)
admin.site.register(EventType)