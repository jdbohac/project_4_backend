from django.urls import path
from . import views

urlpatterns = [
    path('api/games', views.GameList.as_view(), name='game_list'),
    path('api/games/<int:pk>', views.GameList.as_view(), name='game_detail'),
    path('api/users', views.UserList.as_view(), name='user_list'),
    path('api/users/<int:pk>', views.UserList.as_view(), name='user_detail')
]