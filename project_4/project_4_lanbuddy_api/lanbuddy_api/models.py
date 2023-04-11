from django.db import models

# Create your models here.


class User(models.Model):
    name= models.CharField(max_length=32)
    tag= models.CharField(max_length=32)
    availability= models.CharField(max_length=32)
    time_zone= models.CharField(max_length=32)
    skill_level= models.CharField(max_length=32)
    
    def __str__(self):
        return self.tag
        

class Game(models.Model):
    name = models.CharField(max_length=60)
    release_date = models.CharField(max_length=32)
    img = models.TextField()
    game_genre = models.CharField(max_length=32)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
