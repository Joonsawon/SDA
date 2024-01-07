from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def index(request):
#    return HttpResponse("Prayer Music Player")


# Create your views here.
from django.shortcuts import render, redirect

# imported our models
from django.core.paginator import Paginator
from . models import Song

def index(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"PMP_index.html",context)

from django.http import JsonResponse, StreamingHttpResponse

def index2(request):
    paginator= Paginator(Song.objects.all(),1)
    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"PMP_index2.html",context)