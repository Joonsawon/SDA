from django.urls import path
from offering import views

urlpatterns = [
    path('', views.mainHome),
]
