from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request) :
    question_list = Question.objects.order_by('-create_date')
    # 작성 날짜 역순 출력을 위해 order_by를 사용했다('-'라 작석일시의 역순)
    context = {'question_list' : question_list}
    # 모델 데이터를 context에 저장

    # request는 장고에 의해 전달되는 HTTP 요청 객체이다
    # request는 사용자가 전달한 데이터를 확인할 때 사용된다.
    #return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

    return render(request, 'pybo/question_list.html', context)
    # context 모델 데이터를 pybo/question_list.html 템플릿에 출력

def detail(request, question_id) : # question_id는 URL 매핑에 있던 question_id이다.
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id=question_id) # 매개변수의 오프젝트 id값을 가져온다
    question = get_object_or_404(Question, pk=question_id)
    # 모델 기본키로 모델 객체를 반환하고 없으면 404 페이지를 반환한다.
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)