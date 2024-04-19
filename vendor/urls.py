from django.contrib import admin
from django.urls import path
from vendor import views 
urlpatterns = [
    path('',views.index , name='vendor'),
    path('signin/',views.signin , name='signin'),
]
