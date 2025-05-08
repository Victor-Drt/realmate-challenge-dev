from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Conversation, Message
from .serializers import ConversationSerializer, ConversationDetailsSerializer
from django.utils.dateparse import parse_datetime


# Create your views here.
class WebWhook(APIView):
    
    def post(self, request):
        data = request.data
        
        event_type = data.get('type')
        event_timestamp = data.get('timestamp')
        event_data = data.get('data', {})
                
        if event_type == 'NEW_CONVERSATION':
            
            if Conversation.objects.filter(id=event_data['id']).exists():
                return Response({'message': 'Conversa já existe'}, status=400)
            
            new_conversation = Conversation.objects.create(
                id=event_data['id'],
                status='OPEN',
                started_at=parse_datetime(event_timestamp)
            )
        elif event_type == 'CLOSE_CONVERSATION':
            
            try:
                conversation = Conversation.objects.get(id=event_data['id'])
            except Conversation.DoesNotExist:
                return Response({'message': 'Conversa não encontrada'}, status=400)
            
            conversation.status = 'CLOSED'
            conversation.closed_at = parse_datetime(event_timestamp)
            conversation.save()
        elif event_type == 'NEW_MESSAGE':

            try:
                conversation = Conversation.objects.get(id=event_data['conversation_id'])
            except Conversation.DoesNotExist:
                return Response({'message': 'Conversa não encontrada'}, status=400)
            
            if conversation.status == 'CLOSED':
                return Response({'message': 'Esta conversa não pode receber mais mensagens'}, status=400)
                
            if Message.objects.filter(id=event_data['id']).exists():
                return Response({'message': 'Mensagem já registrada'}, status=400)
        
            message = Message.objects.create(
                id=event_data['id'],
                direction=event_data['direction'],
                content=event_data['content'],
                conversation=conversation,
                timestamp=parse_datetime(event_timestamp)
            )
        else:
            return Response({'message': 'Tipo de evento não reconhecido'}, status=404)
        
        return Response({'message': 'Evento processado com sucesso'}, status=200)
    
class ConversationsView(APIView):
        
    def get(self, request):
        
        try:
            conversations = Conversation.objects.order_by('-started_at')
        except Conversation.DoesNotExist:
            return Response({'message': 'Conversa não encontrada'}, status=400)
        
        serializer = ConversationSerializer(conversations, many=True)

        return Response(serializer.data, status=200)
    
class ConversationDetailView(APIView):
        
    def get(self, request, id):
        
        try:
            conversation = Conversation.objects.get(id=id)
        except Conversation.DoesNotExist:
            return Response({'message': 'Conversa não encontrada'}, status=400)
        
        serializer = ConversationDetailsSerializer(conversation)

        return Response(serializer.data, status=200)