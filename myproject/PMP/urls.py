from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

app_name = "PMP"

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.index2, name="index2")
]