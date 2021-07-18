from django.urls import path, re_path , register_converter
from .converters import FourDigitYearConverter  
from .import views
from .views import item_list

register_converter(FourDigitYearConverter,'yyyy')

app_name='shop'

urlpatterns=[
    path('archives/<yyyy:year>/', views.archives_year,name='archives_year'),
    path('',views.item_list,name='item_list'),
    path('<int:pk>/',views.item_detail,name='item_detail'),
    #path(r'^(?P<pk>\d+)/$',views.item_detail), 위와 같은 선언
    path('new/',views.item_new,name='item_new'),
    path('<int:pk>/edit/',views.item_edit,name='item_edit'),

]