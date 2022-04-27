from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name="index"),
    path('about', views.about_view, name="about"),
    path('login', views.login_view, name="login"),
    path('team', views.team_view, name="team"),
    path('profile', views.profile_view, name="profile"),
    path('my_nft', views.my_nft_view, name="my_nft"),
]