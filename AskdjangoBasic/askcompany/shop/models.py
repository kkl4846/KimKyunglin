from django.db import models
#모델 클래스명은 단수형으로 지정
#첫 글자를 대문자로 네이밍

class Item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)   #빈경우도 허용하겠다.
    price=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

