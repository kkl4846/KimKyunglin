from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name='idea'


urlpatterns=[
    path('',views.idea_list,name='idea_list'),
    path('idea/<int:pk>/',views.idea_detail,name='idea_detail'),
    path('idea/create/',views.idea_create,name="idea_create"),
    path('idea/upate/<int:pk>',views.idea_update,name='idea_update'),
    path('idea/delete/<int:pk>',views.idea_delete,name='idea_delete'),
#    path('interest/',views.idea_interest,name="idea_interest"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

