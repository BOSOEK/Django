from django.db import models
from django.urls import reverse
import uuid


class MyModelName(models.Model):
    # Model 클래스에서 파생된 모델을 정의하는 일반적인 클래스

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...
    # CharField : 이 필드가 영숫자 문자열을 포함
    # max_length=20 : 이 필드 값의 최대 길이는 20자임
    # help_text = 'Enter field documentation' : 사용자들에게 알려주기 위해 보여주는 텍스트 라벨 제공

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        # 모델 이름의 특정 인스턴스에 액세스하기 위한 URL을 반환합니다
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        # 모델 이름 개체를 나타내는 문자열(관리사이트 등)
        return self.field_name

# 장르(Genre) 모델 : 책 카테고리에 관한 정보를 저장
class Genre(models.Model) :
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name

class Book(models.Model) :
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # 책은 한 명의 저자 만 가질 수 있지만 저자는 여러 권의 책을 가질 수 있으므로 외래 키 사용
    # null=True : 어떤 저자도 선택되지 않았다면 데이터베이스에 Null 값을 저장
    # on_delete=modles.SET_NULL : 관련 저자 레코드가 삭제되었을때 저자의 값을 NULL로 설정

    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    # isgn의 라벨을 ISBN으로 지정

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    # 장르는 책이 여러 개의 장르를 가지고, 장르도 여러 개의 책을 가질 수 있는 다대다 필드(ManyToManyField)입니다

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 모델의 세부 레코드에 접근하는 데에 사용될 수 있는 URL을 반환환
       return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

class BookInstance(models.Model) :
    # 누군가 빌릴지도 모를 특정한 책의 복사본
    # 필드 : 사용 가능 여부, 언제 돌려받을수 잇는지, 출판사(imprint), 버전 세부 사항, 책의 고유 id

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    # UUIDField는 id필드가 이 모델의 primary_eky로 설정되는 사용한다.
    # 이 타입의 필드는 각 인스턴스에 전역적으로 고유한 값을 할당한다

    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    # 연관된 책을 식별하기 위해(복사본은 하나의 책만 가질 수 있다)

    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    # DataField는 만기일(due_back) 날짜에 사용된다

    LOAN_STATUS = (
        ('m', 'Maintenance'),  # 유지 관리
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta :
        # 레코드들이 쿼리에서 반환시 레코드 정렬을 위해 만기일 필드를 사용한다.
        ordering = ['due_back']

    def __str__(self):
        # 고유햔 id와 연관된 Book의 제목을 조합하여 BookInstance객체를 나타낸다
        return f'{self.id} ({self.book.title})'

class Author(models.Model) :
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
