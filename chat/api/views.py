import imp
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView
)

from chat.models import Chat, Contact, User
from .serializers import ChatSerializer


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    contact = get_object_or_404(Contact, user=user)
    return contact


class ChatListView(ListAPIView):
    serializer_class = ChatSerializer
    permissions_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = Chat.objects.all()
        username = self.request.query_params.get('username')
        if username is not None:
            contact = get_user_contact(username)
            queryset = contact.chats.all()
        return queryset


class ChatDetialView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permissions_classes = (permissions.AllowAny,)


class ChatCreatetView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permissions_classes = (permissions.IsAuthenticated,)


class ChatUpdateView(UpdateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permissions_classes = (permissions.IsAuthenticated,)


class ChatDestroyView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permissions_classes = (permissions.IsAuthenticated,)
