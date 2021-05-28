from django.urls import path

from . import views

"""
config/urls에서 pybo/에 대한 처리를 한 상태라 pybo/를 제외하고 코드를 짠다.
"""

app_name = 'pybo' # 파일 네임스페이스 지정

urlpatterns = [
    path('', views.index, name='index'),  # pybo/로만 오면 index함수를 실행한다
    # 'pybo/'는 index로 사용가능
    path('<int:question_id>/', views.detail, name='detail'), # Question 데이터중 id에 맞는 화면을 보여줌
    # pybo/2/가 실행되면 question_id에 2가 저장되고 views.detail함수가 실행된다.
    # 'pybo/2/'는 detail으로 사용가능

    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]

