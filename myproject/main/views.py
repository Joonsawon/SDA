from django.shortcuts import render, HttpResponse
import random
from .models import User

def index(request):
    return HttpResponse('<h1>Hello, Django!!<h1>'+str(random.random()))

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)

# SDA means stand?

def user_view(request):
    user_instance_list = User.objects.all()

    return render(request, 'index.html', {'user_instance_list': user_instance_list})

