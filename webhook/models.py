from django.db import models

# Create your models here.
class Conversation(models.Model):
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=6, choices=[("OPEN", "OPEN"), ("CLOSED", "CLOSED")])
    started_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True)


class Message(models.Model):
    id = models.UUIDField(primary_key=True)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    direction = models.CharField(max_length=10, choices=[('RECEIVED', 'RECEIVED'), ('SENT', 'SENT')])
    content = models.CharField(max_length=255, null=False)
    timestamp = models.DateTimeField()
