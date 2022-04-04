from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name="index"),
    path('about', views.about_view, name="about"),
    path('login', views.login_view, name="login"),
    path('team', views.team_view, name="team"),
    path('creator', views.creator_view, name="creator"),
]