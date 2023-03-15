from django.urls import path
from . import views

urlpatterns = [
     path('registercustomer', views.registercustomer, name='registercustomerapi'),
     path('logincustomer', views.logincustomer, name='logincustomerapi'),
     path('logoutcustomer', views.logoutcustomer, name='logoutcustomerapi'),
     ]