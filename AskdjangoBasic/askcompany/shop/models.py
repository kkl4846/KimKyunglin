from django.db import models

#08강에서 shell 실행하려면 Item객체 생성해줘야해서 추가
class Item(models.Model):
    name=models.CharField(verbose_name='이름',max_length=100)
    def __str__(self):
        return self.name