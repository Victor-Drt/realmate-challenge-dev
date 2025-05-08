from django.urls import path
from .views import WebWhook, ConversationsView, ConversationDetailView

urlpatterns = [
    path('webhook/', WebWhook.as_view(), name='webhook'),
    path('conversations/', ConversationsView.as_view(), name='conversations'),
    path('conversations/<str:id>', ConversationDetailView.as_view(), name='conversation'),
] 