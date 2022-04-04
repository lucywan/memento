from django.urls import path
from . import views


urlpatterns = [
    path('', views.museum_view, name="museum"),
]