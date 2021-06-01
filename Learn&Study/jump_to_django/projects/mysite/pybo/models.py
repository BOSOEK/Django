from django.db import models

# Create your models here.
class Question(models.Model) :
    # 질문 모델
    subject = models.CharField(max_length=200)
    # 제목 최대 200줄로 설정
    content = models.TextField()
    # 글자 수 제한 없음
    create_date = models.DateTimeField()
    # 날짜 * 시간 속성

    def __str__(self):  # 데이터 조회시 나오는 값
        return self.subject # 데이터 조회시 제목 표시

class Answer(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 왜래키로 다른 모델 속성 가지기(모델 연결), on_delete=models.CASCADE는 답변의 질문이 삭제시 답변도 함께 삭제
    content = models.TextField()
    create_date = models.DateTimeField()