from django.db import models
from django.conf import settings
from django.urls import reverse
class Idea(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(blank=True ,upload_to="idea_image/%Y/%m/%d/")
    content=models.TextField(blank=True)
    interest=models.IntegerField(default=0)
    devtool=models.ForeignKey(verbose_name="예상 계발툴",to='devtool.Devtool',on_delete=models.SET_NULL, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

