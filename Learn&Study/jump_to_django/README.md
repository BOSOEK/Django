# 점프 투 장고 정리
> 점프 투 장고에서 배운점 정리하기
***
## 2-1 주소와 화면 연결 URL & 뷰
> URL과 뷰를 1대 1로 연결하기   

* 요청 URL와 뷰 함수 1대1 매칭
    > 입력 URL에 일치하면 뷰 함수를 실행시킨다
    ```
    from pybo import views
    urlpatterns = [
        path('pybo/', views.index),  
    ]
    ```
    > path의 URL뒤에 '/'를 붙이면 사용자가 주소 입력시 자동으로 '/'를 입력해준다.

* 프로젝트 URL로 시작시 모든 요청을 프로젝트의 urls.py에 매핑하기
    ```
    from django.urls import path, include
    urlpatterns = [
        path('pybo/', include('pybo.urls')),
    ]
    ```
    > pybo/urls.py에서 url 매핑시에는 config/urls에서 'pybo/'를 처리했기에 'pybo/'는 쓰지 않는다

* makemigrations : 장고가 테이블 작업 수행을 하기 위한 파일을 생성한다
* migrate : 실제 테이블 생성 명령이다
> 위의 두 명령어는 모델의 속성이 추가 & 변경시에만 실행한다. 즉, 메서드 등을 추가한 경우에는 실행하지 않는다.

## 2-2 데이터를 관리하는 모델

