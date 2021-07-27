from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name='instagram'

urlpatterns=[
    path('',views.post_list,name='post_list'),
    path('post_create/',views.post_create,name='post_create'),
    path('like_ajax/',views.like_ajax, name='like_ajax'),
    path('comment_create/',views.comment_create,name='comment_create'),
    path('comment_delete/',views.comment_delete,name='comment_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)