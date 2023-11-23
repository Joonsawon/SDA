from django.contrib import admin
from django.urls import path, include
from 스도쿠 import views

urlpatterns = [
    path('', views.스도쿠)
]