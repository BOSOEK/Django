from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request) :
    # request는 장고에 의해 전달되는 HTTP 요청 객체이다
    # request는 사용자가 전달한 데이터를 확인할 때 사용된다.
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")