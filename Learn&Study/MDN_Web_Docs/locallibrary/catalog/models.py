from django.db import models
from django.urls import reverse


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