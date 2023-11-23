from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('Welcome!')

def 스도쿠(request):
    article = '''
        <input type="int" name="title placeholder="배열사이즈(정수)">
    '''
    return HttpResponse('Welcome!')