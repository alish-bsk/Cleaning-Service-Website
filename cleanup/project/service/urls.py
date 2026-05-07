from django.contrib import admin
from django.urls import path
from .views import ServicesChoose,ServicesSaves,Mail

urlpatterns = [
    path('',ServicesChoose.as_view(),name="bookservices"),
    path('sendmail/', Mail.as_view(), name="sendmail"),     
    path('servicesave/', ServicesSaves.as_view(), name="servicesave"),       
   
    
]