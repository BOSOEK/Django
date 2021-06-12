from django.db import models

# Create your models here.

from django.db import models

# 장고 속성 공식 문서 주소 : docs.djangoproject.com/en/3.0/ref/models/fields/#field-types

class Question(models.Model) :
    #제목, 글자수 제한시에는 CharFiled 사용하면 최대 글자수 200
    subject = models.CharField(max_length=200)
    #내용, 글자수 제한없을때는 TextField사용
    content = models.TextField()
    #작성일시, 시간 관련 속성은 DateTimeField를 사용
    create_data = models.DateTimeField()

    def __str__(self):
        # 데이터 모델 조회 결과에 속성값을 보여주는 메서드
        return self.subject


class Answer(models.Model) :
    #질문, 다른 모델을 속성으로 가지면 ForeignKey(다른 모델과의 연결)를 사용
    #on_delete = modles.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
