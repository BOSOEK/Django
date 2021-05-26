"""
config/urls.py는 페이지 요청시 가장 먼저 호출된다.
요청 URL과 뷰함수를 1:1로 매칭한다

URL은 'localhost:8000/pybo'처럼 있을때 호스트명과 포트 번호는 생략된다.
이는 장고 실행 환경에 따라 달라지며 장고가 이미 알고 있기 때문이다

path 함수에서 URL위에 '/'를 붙이면 사용자가 '/'없이 주소 입력시 자동으로 '/'를 붙여준다

"""

from django.contrib import admin
from django.urls import path
from pybo import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),  # pybo/로 시작되는 페이지 요청을 모두 pybo/urls.py 파일의 URL 매핑 참고
    # path('pybo/', views.index)path로 pybo/URL과 views.index(views 파일의 index 함수)를 매핑

]
