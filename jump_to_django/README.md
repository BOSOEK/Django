# 점프 투 장고 정리
> 점프 투 장고에서 배운점 정리하기
***
## 2-1 주소와 화면 연결 URL & 뷰
> URL과 뷰를 1대 1로 연결하기   

* #### 요청 URL와 뷰 함수 1대1 매칭
    > 입력 URL에 일치하면 뷰 함수를 실행시킨다
    ```
    from pybo import views
    urlpatterns = [
        path('pybo/', views.index),  
    ]
    ```
    > path의 URL뒤에 '/'를 붙이면 사용자가 주소 입력시 자동으로 '/'를 입력해준다.

* #### 프로젝트 URL로 시작시 모든 요청을 프로젝트의 urls.py에 매핑하기
    ```
    from django.urls import path, include
    urlpatterns = [
        path('pybo/', include('pybo.urls')),
    ]
    ```
    > pybo/urls.py에서 url 매핑시에는 config/urls에서 'pybo/'를 처리했기에 'pybo/'는 쓰지 않는다
  
## 2-2 데이터를 관리하는 모델
> 모델로 데이터 관리하기
* #### 장고에 기본으로 설치된 앱 확인하기
    > config/setting.py에서 현재 __장고 프로젝트에 설치된 앱__ 을 볼 수 있다.
* #### 데이터 베이스 정보 보기
    > config/setting.py의 DATABESES에서 데이터베이스 정보를 볼수 있다.
    ```
    DATABASES {
        'DEFAULT' : {
            'ENGINE' : 'django.db.backends.sqlite3',
            'NAME' : BASE_DIR / 'db.sqlite3', 
        }
    }
    ```
    > 기본으로 장고는 sqllite(파일 형식의 가벼운 데이터베이스)를 사용한다. 
   
    > BASE_DIR : 프로젝트 디렉터리(mysite)
   
* #### 모델 만들기
    > 장고에서 모델은 __클래스로__ 구현하고 속성은 __인스턴스 변수__로 정의한다.
    ```
    # pybo/models.py
    from django.db import models
    class Question(models.Model) :
        속성 1 = models.CharField(max_length=200)
        속성 2 = models. DateTimeField()
    ```
    
    #### 장고 모델 속성 목록
    * models.CharField(max_length=값) : 글자수 제한 텍스트이다(max_length로 최댁 글자 수를 지정한다)
    * models.TextField() : 글자수 제한 없는 텍스트
    * models.DateTimeField() : 시간 관련 속성
    * models.foreignKey(다른 모델, on_delete=models.CASCADE) : 외래키로 연결할 다른 모델을 매개변수로 받기 on_delete로 연결된 모델 삭제시 함께 사라지게 설정 가능하다
        
    > 모델 데이터 조회 결과에 보여줄 속성값을 선택할 수 있다.
    ```
    def __str-_(self) :
        return self.속성 # 보여줄 속성값
    ```
* #### 앱 등록하기
> 만든 모델로 테이블을 생성하려면 config/setting.py의 INSTALLED_APPS에 내 프로젝트를 추가해야 한다   
    ```
    # config/setting.py   
    INSTALLED_APPS = [    
    '앱이름.apps.앱의 apps.py안의 클래스'    
    ]    
    ```   
> 앱의 apps.py 안의 클래스는 INSTALLED_APPS에 등록하지 않으면 앱 인식 안되고, 데이터베이스 작업도 못한다.

* #### 테이블 작업 파일 생성하기
> makemigrations : 모델 생성 & 수정하여 테이블을 생성할 시 테이블 작업 파일을 만든다.   
    ```   
    python manage.py makemigrations   
    ```   
    > migrations폴더에 파일 생성됨.   
* #### 테이블 생성하기
> migrate로 테이블을 생성할 수 있다.

* makemigrations : 장고가 테이블 작업 수행을 하기 위한 파일을 생성한다
* migrate : 실제 테이블 생성 명령이다
> 위의 두 명령어는 모델의 속성이 추가 & 변경시에만 실행한다. 즉, 메서드 등을 추가한 경우에는 실행하지 않는다.

* #### 데이터 조회하기
> 장고 셸로 데이터 저장 및 조회 가능   
    * 먼저 앱.models에서 모델들을 임포트한다.   
    ```   
    from 앱.models import 모델, 모델   
    ```   
    * 모델로 데이터 만들고 저장하기   
    > 장고는 데이터에 자동으로 ID값을 1부터 넣는다   
    ```   
    q = 모델(속성1='내용', 속성2 = 값)   
    q.save() # 값 저장   
    ```    
* #### 모델 데이터 조회
> 모델.objects.all()으로 모든 데이터들을 출력할 수 있다.   
    * filter로 데이터 조회하기   
    > filter는 여러개의 결과물이 출력되며 조건이 없으면 공백이 출력된다   
    ```   
    모델.objects.filter(속성=값)   
    ```   
    * get로 데이터 조회하기    
    > get은 한개의 결과물이 출력되며 조건이 없으면 에러가 출력된다   
    ```   
    모델.objects.get(속성=값)   
    ```   
* #### 모델 데이터 수정 & 삭제
> 조회로 데이터를 객체에 받은 후 수정이나 삭제를 할 수 있다.   
    ```   
    q = 모델.objects.get(조건)   
    q.속성 = 값   # 값 변경   
    q.save()    # 값 저장   
    q.delete()    # 값 삭제   
    ```   
* ### 연결 데이터 조회   
> 1 : n 연결 데이터에서 서로를 이용행 데이터찾기   
    * n 입장의 데이터에서는 ```객체.속성```으로 얻을 수 있다   
    * 1 입장의 데이터에서는 ```객체.상대모델_set.all()```으로 얻을 수 있다.   
    
## 2-3 장고 Admin 사용하기    
> ```python manage.py createsuperuser```로 어드민 계정을 만들 수 있다.

> localhost:8000/admin에서 관리자 사이트 접속 가능하다

* #### 모델 데이터 관리하기
    > 모델 데이터를 추가, 제거 할 수 있다.
    ```
    # 앱/admin.py
    
    admin.site.register(모델)
    ```
* #### 데이터 검색 기능 추가하기
    > 데이터를 속성 값으로 검색 할 수 있게 한다.
    ```
    class 모델Admin(admin.ModelAdmin) :
        search_fields = ['속성'] 
    ```
## 2-4 질문 목록과 질문 상세 기능 구현하기
* #### 질문 목록 구현하기
    > ```render(request, '파일', 모델 데이터)'```함수를 리턴하여 페이지에 데이터 정보를 보낸다
* #### 템플릿 만들기
    > 템플릿을 저장할 폴더를 만들면 settings.py의 TEMPLATES의 항목이 'DIRS'를 ```[BASE_DIR / '폴더명]``` 형태로 등록한다
    ```
    # 템플릿 파일 예제
    {% if question_list %}  # question_list가 있다면
        <ul>
        {% for question in question_list %}
            <li><a href="/pybo/{{ question.id }}/">{{ question.subject }}</a></li>
        {% endfor %}
        </ul>
    {% else %}  # question_list가 없다면
        <p>질문이 없습니다.</p>
    {% endif %}
    ``` 
* #### 오류 화면 구현하기
    > 함수에서 모델 데이터를 받을때 ```모델.objects.get(변수=속성)``` 대신 ```get_object_or_404(모델, pk=속성)```으로 수정한다
  
    > pk에 해당 건이 없으면 404 페이지를 출력한다. 
## 2-5 URL 더 똑똑하게 사용하기
> 주소에 url을 직접 지정하면 주소가 바꼈을때 일일이 다 바꿔줘야 한다.
* #### 네임 스페이스 추가하기
    > 한 프로젝트에 앱이 여러개가 생기면 다른 앱에서 URL 중복이 생긴다
    ```앱/urls.py```에 ```app_name = '앱'``` 으로 네임스페이스를 추가한다.
* #### URL 별칭 사용하기
    > 앱의 urls.py의 path에서 ```name='별칭'```형태로 별칭을 지정한다.
* #### 템플릿에서 URL 별칭 사용하기
    > 주소 지정창에서 ```{% url '네임스페이스:URL 별칭' 매개변수` %}``` 형태로 사용한다
## 2-6 답변 등록 기능 만들기
* #### html에서 정보 전송
    >답변 전송을 위해 ```form```을 이용하며 폼 태그 안에는 ```{% csrf_token %}```을 항상 사용하여 보안을 유지야하고 폼 태그의 매개변수로 action에 url과 매개변수를 넘길 수 있다.
* #### redirect
    > 페이지 이동을 수행하며 첫번째 인수로 이동할 페이지 별칭, 두번째 인수로 전달할 값을 갖는다
## 2-7 style 적용하기
* #### 스태틱 디렉터리 위치 추가
    > config/settings.py의 static_url에 만든 스태틱 폴더를 입력한다
    > STATICFILES_DIRS에 ```BASE_DIR / '폴더이름',``` 을 입력하여 스태틱 디렉터리 위치를 추가한다.
* #### 스태틱 스타일 적용하기
    > 템플릿 위에 ```{% load static %} <link rel="stylesheet" type="text/css" href="{% 폴더 파일름 %}"``` 으로 스타일을 적용한다
## 2-9 템플릿 상속 이용하기
* #### 템플릿 상속
    > 기본의 html 템플릿을 작성후 body 태그 안을 ```{% block content%} {%  endblock %}``` 으로 묶고 다른 html 파일에서 ```{% extends 템플릿 %}``` 으로 불러온후 똑같이 block으로 묶어서 템플릿 안의 내용을 쓴다
***
## 3장부터는 파이보 서비스의 업그레이드 버전이다.