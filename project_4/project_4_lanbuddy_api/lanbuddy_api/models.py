from django.db import models
import django_filters
# Create your models here.


class Game(models.Model):
    name = models.CharField(max_length=60)
    release_date = models.CharField(max_length=32)
    img = models.TextField()
    game_genre = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class User(models.Model):
    user_name = models.CharField(max_length=32)
    tag = models.CharField(max_length=32)
    availability = models.CharField(max_length=32)
    time_zone = models.CharField(max_length=32)
    skill_level = models.CharField(max_length=32)
    game = models.ForeignKey(Game, related_name='players', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tag

class GameFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Game
        fields = ["game_genre"]