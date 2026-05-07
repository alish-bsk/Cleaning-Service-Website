from django.contrib import admin
from django.urls import path
from .views import MailDes


urlpatterns = [
path('maildescription/', MailDes.as_view(), name="maildes"),
]