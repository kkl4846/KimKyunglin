from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name='devtool'


urlpatterns=[
    path('',views.devtool_list,name='devtool_list'),
    path('create/',views.devtool_create,name="devtool_create"),
    path('<int:pk>/',views.devtool_detail,name="devtool_detail"),
    path('update/<int:pk>/',views.devtool_update,name="devtool_update"),
    path('delete/<int:pk>/',views.devtool_delete,name="devtool_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

