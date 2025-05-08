from rest_framework import serializers
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'conversation', 'direction', 'content', 'timestamp']

class ConversationDetailsSerializer(serializers.ModelSerializer):

    messages = MessageSerializer(many=True)
    
    class Meta:
        model = Conversation
        fields = ['id', 'status', 'messages']
        
class ConversationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Conversation
        fields = ['id', 'status', 'started_at', 'closed_at']
