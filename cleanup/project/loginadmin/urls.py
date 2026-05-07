from django.contrib import admin
from django.urls import path
from .views import LoginAdmin,LogoutAdmin


urlpatterns = [
path('login/', LoginAdmin.as_view(), name="loginadmin"),
path('logout/', LogoutAdmin.as_view(), name='logoutadmin'),
]