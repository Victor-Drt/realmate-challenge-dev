from rest_framework import serializers
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.

    Serializes and deserializes Message instances,
    including fields such as direction, content, and timestamp.
    """
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'direction', 'content', 'timestamp']


class ConversationDetailsSerializer(serializers.ModelSerializer):
    """
    Detailed serializer for Conversation model.

    Includes all messages associated with the conversation.
    Useful for retrieving a conversation and its full message history.
    """

    messages = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['id', 'status', 'messages']


class ConversationSerializer(serializers.ModelSerializer):
    """
    Basic serializer for Conversation model.

    Used for creating and listing conversations,
    with optional timestamps for start and closure.
    """

    class Meta:
        model = Conversation
        fields = ['id', 'status', 'started_at', 'closed_at']
