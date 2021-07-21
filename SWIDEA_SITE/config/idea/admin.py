from django.contrib import admin
from .models import Idea


@admin.register(Idea)
class CustomIdeaAdmin(admin.ModelAdmin):
    pass