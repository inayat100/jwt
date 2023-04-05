from django.urls import path
from .views import UserSignUp,UserSignin
urlpatterns = [
    path('signup/',UserSignUp.as_view(),name="Signup"),
    path('signin/',UserSignin.as_view(),name="Signin")
]