from django.shortcuts import render, HttpResponse
import random

def index(request):
    return HttpResponse('<h1>Hello, Django!!<h1>'+str(random.random()))

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)