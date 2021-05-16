# MDN Web Docs의 장고 튜토리얼
> 링크 : https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/skeleton_website
* 본 튜토리얼은 책 빌리는 도서 웹 사이트 제작을 목표로 한다.
## 목차
* ### [Part 3. 모델 생성하기](#part-3)
* ### [Part 4. 관리자 사이트 만들기](#part-4)
***

## Part 3
> 필드를 사용하여 모델을 설계 & 생성
* 장고는 __모델__ 이라는 파이썬 객체로 데이터에 접속하고 관리하며 모델은 저장된 __데이터의 구조__ 를 정의한다.

### 1. 모델의 정의
> 모델은 보통 어플리케이션의 models.py 파일에서 정의하며 ```django.db.models.Model```의 서브 클래스로 구현되고 필드, 메소드, 메타데이터들을 포함할 수 있다.
* ### 필드
    > 모델의 필드는 데이터 베이스에 저장하는 데이터 열을 의미한다.
    ```
    # 예시
    field = models.CharField(max_length=20, help_text='Enter')
    # max_length : 필드의 최대 길이 지정
    ```
    > 위 예시는 영숫자 문자열을 포함하는 ```models.CharField``` 타입의 ```field```라는 필드를 하나 만들었다.  

    * __필드 타입 : 특정 클래스들을 사용하며 값 수신 시 사용할 유효성 검증 기준과 데이터베이스에 저장되는 데이터의 타입을 결정한다.(필드 타입 목록 : https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)__
    * __필드 인수 : 필드 타입이 지정하며 어떻게 저장되고 사용될지 지정한다.(필드 옵션 목록 : https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-options)__
* ### 메타데이터
    * ```class Meta```를 선언하여 모델에 대한 모델-레벨의 메타데이터 선언가능하다.

    __메타 데이터 옵션(메타 데이터 옵션 목록 : https://docs.djangoproject.com/en/2.0/ref/models/options/)__
    * 모델 타입을 쿼리(저장)할 때 반환되는 기본 레코드(행) 순서를 제어하기(저장시의 순서 정렬)
        ```
        class Meta :
            ordering = ['-my_field_name']
        ```
        > 정렬 순서를 지정하려면 ```ordering```속성에 지정하며 정방향 정렬(문자는 알파벳 순대로, 숫자는 작은 순대로) 하려면 그냥 쓰고 역순대로 정렬하려면 필드 이름 앞에 '-'기호를 붙인다.

        > 아래처럼 복수 정렬도 가능하다
        ```ordering = ['title', 'pubdata'] #타이틀은 A-Z순대로 이후 pubdata순대로 정렬됨```

        __이외에도 '접급 권한' 생성 및 적용도 되고 클래스가 추상 클래스임을 선언도 가능하다__
* ### 메소드
    __최소한, 모든 모델마다 __str__()을 정의하여 각각의 object가 문자열을 반환하도록 한다.__
    * ```get_absolute_url()``` : 웹사이트의 개별적인 모델 레코드(행)들을 보여주기 위한 URL을 반환하는 메소드
    ```
    def get_absolute_url(self) :
        return reverse('model-detail-view), args=[str(self.id)]
    ```
### 2. 모델의 관리
* ### 레코드의 생성과 수정
    >레코드(데이터베이스의 행(새로운 데이터))를 생성(저장)하려면 모델의 인스턴스를 정의하고 ```save()``` 를 호출한다.
    ```
    레코드 명 = 나의 모델이름(나의 필드 이름='필드 명')
    레코드.save()
    ```
    > 만약 어떤 필드도 ```primary_key```를 선언하지 않으면 저장시에 자동으로 id라는 필드를 만든다.

    > 레코드 안의 필드에 '.'을 이용해 접근할 수 있고 저장시에는 ```save()```를 사용한다.
* ### 레코드의 검색
    > 모델의 객체 속성을 사용하여 특정 기준과 일치하는 레코드를 검색 할 수도 있다.
    * ```objects.all()``` : 모델의 모든 레코드들을 QuerySet으로 가져올 수 있다.
    * ```filter()``` : 반환된 쿼리 셋을 지정한 문자 또는 숫자 필드를 특정 기준으로 필터링 가능하다
    ```
    test = 모델명.objects.filter(속성 = '값')
    ```
    > filter의 속성
    * ```필드명__contains = '값'``` : 값(대소문자 구별)을 포함하는 필드들을 가져옴(모든 일치 방법 목록 : https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups)
    
    > 외래키를 이용한 필터링
    ```
    변수 = 모델.objects.filter(외래키 모델__필드명__속성 = '값')
    ```
    > 그 외의 쿼리 : https://docs.djangoproject.com/en/2.0/topics/db/queries/
    
### 3. 데이터 마이그레이션
* ### 장고는 __ORM(Object-Relational-Mapper : 객체-관계-매퍼)__ 사용하여 모델 정의를 기본 데이터베이스에서 사용하는 데이터 구조에 매핑한다
    > 모델의 정의를 바꿀때마다 장고는 변화를 추적, 데이터베이스 안의 기본 데이터 구조가 모델과 일치하도록 자동으로 이전하는 스크립트(migrations)를 생성한다. 
* ### 데이터 마이그레이션 실행
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
    * ```makemigrations``` : 프로젝트에 설치된 모든 앱에 대한 migration을 생성하며 적용되지는 않는다
    * ```migrate``` : 실제 데이터베이스에 적용된다.
***
## Part 4
> 장고 관리자 사이트 이해, 모델을 위한 레코드 생성하기
* ### 1. 모델 등록하기
    > 관리자 사이트에서 모델을 테스트하기 위해 모델을 사이트에 등록해야 한다.
    * ```models.py```에서 만든 모델을 ```admin.py```에서 ```admin.site.register(모델)```로 호출하여 등록한다.
* ### Superuser 만들기
    > 관리자 사이트 로그인을 위해서는 직원 상태의 사용자 계정이 필요하다.(사이트 접속 권한은 ```manage.py```를 사용해서 만들 수 있다.)
    * 직원 계정은 ```createsuperuser```로 만들 수 있다.
    ```
    python manage.py createsuperuser
    ```
    * 이제 관리자 사이트(```localhost:8000/admin```)으로 접속하여 모델 관련 레코드를 생성 & 수정 가능하다
* ### 추가 설정
    > 장고는 등록된 모델 정보로 관리자 사이트를 만들 수 있다.
    * 각각의 모델은 모델의 ```__str__()```메소드로 생성된 세부 정보/양식에 링크되어 있는 개별 레코드 목록을 가지고 있다.
    * 레코드 편집 & 추가를 위한 디테일 레코드 양식들은 모델 안의 모든 필드를 포함하며 수직으로 배치된다.
    
    > 사용성을 위해 인터페이스를 추가할 수 있다.
    * 목록 뷰(List views)
        * 각각의 레코드의 추가적인 __필드/정보 추가__
        * 날짜나 다른 선택값에 기초해 어던 레코드들이 목록지어질 지 선택하는 __필터 추가__
        * 목록 뷰 안의 동작 메뉴에 옵션 추가 및 양식 위의 __어디에 보여질지 선택__ 하기
    * 세부 뷰(detail views)
        * 표시&제외할 필드, 순서, 그루핑, 편집 가능 여뷰, 사용 위젯, 방향 등등 선택하기
        * 인라인 편집을 위해 관련 필드들을 레코드에 추가하기
    __그외의 관리자 사이트 사용자화 레퍼런스 : https://docs.djangoproject.com/en/2.0/ref/contrib/admin/__

* ### ModelAdmin 클래스 등록하기
    > 관리자 인터페이스에서 보여지는 방식 변경을 위해서는 ```ModelAdmin``` 클래스를 정의 후 모델 안에 등록한다.
    * 기존의 모델 등록(```admin.site.register(모델)```)을 제거 후 아래처럼 새로운 모델 어드민 클래스를 등록한다.
    ```
    class 이름(admin.ModelAdmin) :
        내용
    admin.site.register(모델, 모델_어드민_클래스) # 관리자 클래스 등록
    ```
    __```admin.site.register(모델)``` 대신 ```@admin.register(모델)```로 사용해도 상관없다__
* ### 목록 뷰 설정하기
    > 각 모델들의 레코드들이 출력될 때 추가적인 정보(레코드)를 보여주고 싶다면 ```list_display```를 이용하여 더 많은 정보를 보여줄 수 있다.
    ```
    class 어드민_클래스_이름(admin.ModelAdmin):
        list_display = ('필드', '필드')
    ```
* ### 목록 필터 추가하기
    > 목록 안의 항목중 어떤 항목이 표시될 지 필터를 추가할 수도 있다. ```list_filter```속성 안에서 필드들을 목록지어 완료된다.
    ```
    class 어드민_클래스_이름(admin.ModelAdmin):
        list_filter = ('필드', '필드')
    ```
    > 위의 코드처럼 필터를 추가하면 목록 뷰 오른쪽에 필터 상자가 생성된다.
* ### 세부 보기 레이아웃 조직하기
    > 기본적으로 세부 레이아웃들은 모델 선언 순서대로 배치되지만 ```fields``` 속성으로 선언 순서, 표시 & 제외 필드 등 변경이 가능하다
    ```
    class 어드민_클래스_이름(admin.ModelAdmin) :
        fields = ['필드', '필드', ('필드', '필드')]
    ```
    > ```fields```속성은 양식에 보여져야 할 필드들을 순서대로 목록을 짓고 기본적으로 수직 표시지만 튜플 안에 묶으면 수평적으로 표시된다

    * ```fieldsets``` : 세부 양식 안의 연관 모델 정보 그룹화를 위해 "sections" 추가
    ```
    class 어드민_모델_클래스(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields' : ('필드1', '필드2', '필드3')
            }),
            ('Add', {
                'fields' : ('필드4', '필드5')
            }),
        )
    ```
    > 위 코드 입력시 양식 창에 필드1, 2, 3이 제목없이(None) 입력 창이 있고 아래에 Add섹션으로 필드 4와 5를 입력할 수 있게 양식이 바뀐다.
* ### 연관 레코드들의 인라인 편집
    > 연관 레코드들을 동시에 추가하기(inlines, TabularInline, StackedInline으로 가능하다)
    ```
    class 어드민_모델_클래스(admin.ModelAdmin) :
        inlines = [인스턴스 모델]
    ```
