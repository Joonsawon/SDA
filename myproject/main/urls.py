from django.urls import path
from main import views

urlpatterns = [
    path('', views.user_view),
    path('create/', views.create),
    path('read/<id>/', views.read)


]
