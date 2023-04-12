from django.shortcuts import render
from rest_framework import generics
from .serializers import GameSerializerBase,GameSerializer, UserSerializer
from .models import Game, User
# Create your views here.
class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    
class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
    
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    