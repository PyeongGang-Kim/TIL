from django.db import models
from django.conf import settings

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)
    class Meta:
        ordering =('-pk',)

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    class Meta:
        ordering=('-pk',)

