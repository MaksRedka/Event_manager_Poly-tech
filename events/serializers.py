from rest_framework import serializers
from .models import Event, EventType


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["id", "user", "event_type", "info", "timestamp", "created_at"]


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ["name"]
