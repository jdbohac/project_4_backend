from django.shortcuts import render
from rest_framework import generics
from .serializers import GameSerializerBase, GameSerializer
# Create your views here.
class GameList(generics.ListCreateAPIView):
    queryset = Game