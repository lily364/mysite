from django.db import models
from django.contrib.auth.models import User
import time


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=130)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(time.localtime, auto_now=True)
    last_updated_time = models.DateTimeField(time.localtime, auto_now_add=True)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

