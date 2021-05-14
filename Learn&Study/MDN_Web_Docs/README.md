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
    


