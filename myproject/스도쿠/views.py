from django.shortcuts import render, HttpResponse
import random

topics = [{'id':1,'title':'Routing','body':'Routing is ..'},
          {'id':2,'title':'View','body':'View is ..'},
          {'id':3,'title':'Model','body':'Model is ..'}]

def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return HttpResponse(f'''
    <h1>스도쿠</h1>
    <ol>
        {ol}
    </ol>
    <h2>Welcome</h2>
    Hello, Django
    ''')

#return HttpResponse('<h1>Random</h1>'+str(random.random()))

def 스도쿠(request):
    article = '''
        <input type="int" name="size" placeholder="배열사이즈(정수)">
    '''
    return HttpResponse(article)

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)