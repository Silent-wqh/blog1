from django.db import models
from django.utils import timezone


class Article(models.Model):
    """
    字段：标题、内容、发表时间、更新时间
    方法：
    """
    title = models.CharField(max_length=30)
    content = models.TextField()

    create_time = timezone.now()
    update_time = timezone.now()

    def __str__(self):
        return self.title
