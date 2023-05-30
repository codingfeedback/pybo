from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')  #추천인 추가

    def __str__(self):
        return self.subject



class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer') #on_delete 글쓴이가 삭제된다면 관련된 콘텐츠도 같이 삭제되도록 설정
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #CASCADE 종속
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')  #추천인 추가
    
