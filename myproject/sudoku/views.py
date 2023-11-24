from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np

import random



def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTamplate(article))

#return HttpResponse('<h1>Random</h1>'+str(random.random()))


@csrf_exempt
def sudoku(request):
    print('request.method', request.method)
    if request.method == 'POST':
        size = int(request.POST['size'])
        수도쿠 = ''
        for i in range(size):
            수도쿠 += f'''<p>{np.concatenate((np.arange(1+i,size+1), np.arange(1,i+1)))}</p>'''
        #수도쿠 = np.array(수도쿠)

        #print(np.random.shuffle(수도쿠))

        article = f'''
                <form action="" method="post">
                    <h1>수도쿠!</h1><p>생성할 수도쿠 배열의 사이즈를 입력해 주세요.</p>
                    <p><input type="number" name="size" placeholder=" 배열사이즈(정수)"></p>
                    <p><input type="submit"></p>
                </form>
                <p>입력한 값: {size}</p>
                <p>{수도쿠}</p>
            '''
        return HttpResponse(article)
    elif request.method == 'GET':
        article = f'''
                        <form action="" method="post">
                            <h1>수도쿠!</h1><p>생성할 수도쿠 배열의 사이즈를 입력해 주세요.</p>
                            <p><input type="number" name="size" placeholder=" 배열사이즈(정수)"></p>
                            <p><input type="submit"></p>
                        </form>
                    '''
        return HttpResponse(article)

        return HttpResponse('')


def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!'+id)


def HTMLTamplate(article):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <h1>스도쿠</h1>
    <ol>
        {ol}
    </ol>
    <h2>Welcome</h2>
    Hello, Django
    '''
## 이렇게?