from django.db import models

# Create your models here.
class Article(models.Model):
    # CharField는 글자수 제한이 필수
    title = models.CharField(max_length=10)
    # TextField는 글자수 제한 필요없음
    content = models.TextField()
    # 최초로 입력될때만 
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트할 때만
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}번글 - {}: {}'.format(self.id, self.title, self.content)
