from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

import uuid

# Create your models here.

class EventType(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True)
    info = models.JSONField()
    timestamp = models.DateField(auto_now_add=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id.__str__()

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)