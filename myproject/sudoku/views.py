from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import random, copy, time



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
        size = int(request.POST['size']) # POST로 넘겨받은 값을 int로 저장 (스도쿠 사이즈)

        # 예외처리
        if size > 10_000:
            size = 10_000
        elif size < 1:
            size = 1

        start = time.time()  # 계산시간 카운트 시작
        random_range = np.arange(size)  # 스도쿠 사이즈 만큼 숫자 배열 생성
        np.random.shuffle(random_range)  # 숫자 배열 셔플 (행 셔플 용)

        수도쿠 = []  # 스도쿠 담을 list 변수 선언
        for i in random_range:
            수도쿠.append(np.concatenate((np.arange(1+i, size+1), np.arange(1, i+1)))) #스도쿠 라인 생성 및 리스트에 행 추가
        수도쿠 = np.array(수도쿠) # 리스트를 넘파이 배열로 변환

        # 열 셔플 실행
        for i in range(size // 5): #전체 크기에 1/5 만큼만 실행
            j = random.randrange(0, size) # 랜덤한 열 선택
            k = random.randrange(0, size) # 랜덤한 열2 선택
            # 열 바꾸기
            임시저장_j = copy.deepcopy(수도쿠[:, j])
            수도쿠[:, j] = 수도쿠[:, k]
            수도쿠[:, k] = 임시저장_j
            #반복.. (for문 사용시간을 줄이기 위함)
            j = random.randrange(0, size)
            k = random.randrange(0, size)
            임시저장_j = copy.deepcopy(수도쿠[:, j])
            수도쿠[:, j] = 수도쿠[:, k]
            수도쿠[:, k] = 임시저장_j
            j = random.randrange(0, size)
            k = random.randrange(0, size)
            임시저장_j = copy.deepcopy(수도쿠[:, j])
            수도쿠[:, j] = 수도쿠[:, k]
            수도쿠[:, k] = 임시저장_j
            j = random.randrange(0, size)
            k = random.randrange(0, size)
            임시저장_j = copy.deepcopy(수도쿠[:, j])
            수도쿠[:, j] = 수도쿠[:, k]
            수도쿠[:, k] = 임시저장_j

        end = time.time() # 끝나는 시간 카운트

        수도쿠출력 = '' # html 담을 문자형 변수 선언
        for i in range(size):
            수도쿠출력 += f'''<p>{수도쿠[i]}</p>''' # 스도쿠 행별로 코드 짜기

        article = f'''
                <form action="" method="post">
                    <h1>수도쿠!</h1><p>생성할 수도쿠 배열의 사이즈를 입력해 주세요.</p>
                    <p><input type="number" name="size" placeholder=" 배열사이즈(정수)"></p>
                    <p><input type="submit"></p>
                </form>
                <p>입력한 값: {size}</p>
                <p>걸린시간: {end - start:.5f} 초</p>
                <p>{수도쿠출력}</p>
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