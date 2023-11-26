"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')), # include 함수를 이용해 main 폴더(app)의 urls.py로 보내준다. (홈 페이지)
    path('admin/', admin.site.urls), # 장고의 기본 관리자 페이지
    path('sudoku/', include('sudoku.urls')) # 수도쿠 미니게임 페이지 (경로 입력으로만 접속 가능한 이스터에그로 활용할 예정)
]

#강대윤 바보
