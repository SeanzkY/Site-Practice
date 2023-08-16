from django.urls import path

from . import views

urlpatterns = [
    path("site", views.index, name="index"),
    path('tictactoe', views.game, name='game'),
]
