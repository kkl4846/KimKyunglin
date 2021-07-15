from django.db import models
from django.conf import settings

"auth.User" #앱에 대한 외래키
#모델 클래스명은 단수형으로 지정
#첫 글자를 대문자로 네이밍

#charfield:길이제한 textfield:길이제한 없음 slugfield:charfield를 상속받은 것. slug(뉴스 기사에 url에 해당 뉴스에 대한 제목이 붙음)목적으로 사용
#파일: FileField: ImageField: 업로드된 파일은 데이터베이스에 저장되지 않음.파일이 저장된 경로를 저장. binaryfield는 성능이 좋지않음. filepathfield: 경로만 저장. 
#email,url -> db입장에서는 charfield
#foreignkey ->일반적인 하나의 포스트에 여러개의 commentmanytomanyfield->다대다 관계
class Item(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(blank=True)   #빈경우도 허용하겠다.
    price=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

