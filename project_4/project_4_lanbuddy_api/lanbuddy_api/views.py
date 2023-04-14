from django.shortcuts import render
from rest_framework import generics
from .serializers import GameSerializerBase,GameSerializer, UserSerializer
from .models import Game, User
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game_genre']
    search_fields = ['name', 'game_genre']

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
