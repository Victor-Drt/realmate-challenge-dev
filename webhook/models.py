from django.db import models

# Create your models here.
class Conversation(models.Model):
    """
    Represents a chat conversation.

    Attributes:
        id (UUID): Unique identifier for the conversation.
        status (str): Status of the conversation, either 'OPEN' or 'CLOSED'.
        started_at (datetime): Timestamp when the conversation started.
        closed_at (datetime): Timestamp when the conversation was closed (nullable).
    """
    id = models.UUIDField(primary_key=True)
    status = models.CharField(max_length=6, choices=[("OPEN", "OPEN"), ("CLOSED", "CLOSED")])
    started_at = models.DateTimeField()
    closed_at = models.DateTimeField(null=True)


class Message(models.Model):
    """
    Represents a message in a conversation.

    Attributes:
        id (UUID): Unique identifier for the message.
        conversation (Conversation): The conversation this message belongs to.
        direction (str): Message direction - 'RECEIVED' or 'SENT'.
        content (str): The message content.
        timestamp (datetime): Time the message was sent or received.
    """
    id = models.UUIDField(primary_key=True)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    direction = models.CharField(max_length=10, choices=[('RECEIVED', 'RECEIVED'), ('SENT', 'SENT')])
    content = models.CharField(max_length=255, null=False)
    timestamp = models.DateTimeField()
