from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import Game, User

class GameSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','release_date','game_genre','img')

class UserSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'tag', 'availability', 'time_zone', 'skill_level')
        
class GameSerializer(GameSerializerBase):
    players = UserSerializerBase(many=True)
    class Meta(GameSerializerBase.Meta):
        fields = GameSerializerBase.Meta.fields + ('players',)
        
class UserSerializer(WritableNestedModelSerializer, UserSerializerBase):
    game = GameSerializerBase()
    class Meta(UserSerializerBase.Meta):
        fields = UserSerializerBase.Meta.fields + ('game',)