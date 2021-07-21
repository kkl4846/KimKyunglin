from django.contrib import admin
from .models import Devtool


@admin.register(Devtool)
class CustomIdeaAdmin(admin.ModelAdmin):
    pass