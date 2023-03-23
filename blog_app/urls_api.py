from django.urls import path
from .views_api import *

urlpatterns = [
    path("login_api/",Login_api_view,name="login_api"),
    path("register_api/",Register_api_view,name="register_api"),
    
]