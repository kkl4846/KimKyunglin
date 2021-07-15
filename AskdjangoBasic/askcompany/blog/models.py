from django.db import models
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    blog_url=models.URLField(blank=True)

class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,db_index=True)
    slug=models.SlugField(allow_unicode=True,db_index=True)
    content=models.TextField(blank=True)
    comment_count=models.PositiveBigIntegerField(default=0)
    tag_set=models.ManyToManyField('Tag',blank=True)
    is_publish=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Comment(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name=models.CharFiedl(max_length=50,unique=True #unique- 같은 이름의 태그는 없다
    
    