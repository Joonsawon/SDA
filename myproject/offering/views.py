from django.shortcuts import render, HttpResponse
import random

# Create your views here.

def mainHome(request):
    return render(request,'offeringIndex.html');