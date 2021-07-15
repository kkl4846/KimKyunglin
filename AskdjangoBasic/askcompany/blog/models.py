from django.db import models
from django.conf import settings
# Create your models here.
#11강 
#python manage.py migrate <앱이름><마이그레이션-이름>
#<마이그레이션-이름>이 마지막 migrate가 되어야함 ex 1 2 3 migrate진행 python manage.py migrate blog 002 이면 3번 migrate는 취소

#이미 migrate를 한 상태에서 추가로 post에 필드를 집어넣는 다면 기존 record들에 어떤 값으로 채워넣을 지 묻는 것- 직접입력/blank
class Post(models.Model):
    author_name=models.CharField(max_length=20,blank=True)  #이때 blank가 기존 record를 blank로 채워넣겠다는 의미
    title=models.CharField(max_length=100,db_index=True)
    content=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE) #on_delete...속해있는 post가 삭제되면 comment도 삭제하겠다라는 의미 
    message=models.TextField()