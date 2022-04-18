from django.urls import path

from .views import register

urlpatterns = [
    # path("signup/", SignUpView.as_view(), name="signup"),
    path("signup/", register, name="signup")
]