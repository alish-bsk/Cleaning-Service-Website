from django.contrib import admin
from django.urls import path
from .views import Record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Record.home_page,name='home'),
    path('residential_page/',Record.residential_page,name='residential'),
    path('bond_page/',Record.bond_page,name='bond'),
    path('lease_page/',Record.findlease_page,name='lease'),
    path('vacate_page/',Record.vacate_page,name='vacate'),
    path('moveout_page/',Record.moveout_page,name='moveout'),
    path('exit_page/',Record.exit_page,name='exit'),
    path('movein_page/',Record.movein_page,name='movein'),
    path('rental_page/',Record.rental_page,name='rental'),
    path('cominst_page/',Record.cominst_page,name='cominst'),
    path('oven_page/',Record.oven_page,name='oven'),






]
