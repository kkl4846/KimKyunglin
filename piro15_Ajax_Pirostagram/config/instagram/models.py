from typing import ContextManager
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.files import ImageField

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(blank=True)
    image=ImageField(blank=True ,upload_to="post_image/%Y/%m/%d/")
    like=models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Comment(models.Model):
    comment_content=models.TextField()
    post=models.ForeignKey("Post",on_delete=CASCADE,related_name="post_comment")
    def __str__(self):
        return self.comment_content
    