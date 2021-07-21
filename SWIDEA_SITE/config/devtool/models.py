from django.db import models

class Devtool(models.Model):
    name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    explain=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
