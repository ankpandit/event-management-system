from django.contrib import admin
from django.urls import path
from user import views  
urlpatterns = [
    path('',views.index , name='user'),
    path('serviceslist/',views.servicelist ,name = 'service') ,
]
