from django.urls import path
from main import views

urlpatterns = [
    path('', views.user_view)
]
