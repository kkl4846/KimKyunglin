from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
      path('post/<int:pk>/', views.post_detail, name='post_detail'), #post/<int:pk/>/는 url 패턴을 나타냄/ post/1 post/2 ..
]