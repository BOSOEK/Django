# MDN Web Docs의 장고 튜토리얼
> 링크 : https://developer.mozilla.org/ko/docs/Learn/Server-side/Django/skeleton_website
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
### 1. 모델의 관리
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
    ```변수 = 모델.objects.filter(외래키 모델__필드명__속성 = '값')

    > 그 외의 쿼리 : https://docs.djangoproject.com/en/2.0/topics/db/queries/
