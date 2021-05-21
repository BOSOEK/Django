from django.urls import path
from catalog import views
# 어플리케이션을 만들면서 패턴들을 이곳에 추가할 것.
urlpatterns = [
    path('', views.index, name='index'),
    # URL 패턴 감지시 호출될 view함수는 views.py 파일 안에서 index()로 이름지어져 있다.
    # path()함수는 name 매개변수를 지정하며, 이름의 매퍼를 반전시킬 수도 있다.
    # 즉, 매퍼가 처리하도록 설계된 URL을 동적으로 생성하기 위해서(페이지 이동 등)

    path('books/', views.BookListView.as_view(), name='books'),
]