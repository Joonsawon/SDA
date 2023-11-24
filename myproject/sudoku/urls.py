from django.contrib import admin
from django.urls import path, include
from sudoku import views


urlpatterns = [
    path('', views.sudoku),
    path('create/', views.create),
    path('read/<id>/', views.read)
]