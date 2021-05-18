# 템플릿과 데이터를 이용해 HTML 파일을 생성하는 render 포함
from django.shortcuts import render

# Create your views here.
# 뷰는 HTTP 요청을 처리하고, 데이터베이스에서 데이터를 가져오고,
# HTML 템플릿으로 데이터를 랜더링하고 생성된 HTML을 HTTP응답으로 반환하여 사용자들에게 보여주는 함수이다.
# (index 뷰는 이 구조(모델)을 따라간다
# index는 데이터베이스 안의 모델들의 레코드 개수 및 정보를 가져오고 그 정보를 템플릿으로 전달한다

from catalog.models import Book, Author, BookInstance, Genre
# 우리의 모든 뷰들 안에서 데이터에 접근하는데 필요한 모델 클래스 import

def index(request) :
    """사이트 홈페이지 보기 기능"""

    # 일부 주요 개체의 개수 생성
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # 모델 클래스들에서 레코드들의 개수를 가져옴

    # 사용 가능한 책(상태)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # 상태 필드에서 'a'값을 가지는 BookInstance 객체들 목록도 가져옴

    # 'all()'은 기본적으로 내포되어 있다
    num_authors = Author.objects.count()

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available' : num_instances_available,
        'num_authors' : num_authors,
    }

    # 컨텍스터 변수의 데이터를 사용하여 HTML 템플릿 index.html을 렌더링한다.
    return render(request, 'index.html', context=context)
    # render() : HTML 페이지 생성 및 페이지를 응답으로 반환하는 함수
    # render()의 매개변수들
    # request : HttpRequest인 원본 객체
    # 데이터에 대한 플레이스홀더들을 갖고 있는 HTML 템플릿
    # context