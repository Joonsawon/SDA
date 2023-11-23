from django.contrib import admin
from django.urls import path, include
from 스도쿠 import views


urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read)
]