from django.urls import path, register_converter
from .converters import FourDigitYearConverter  
from .import views
from .views import item_list

register_converter(FourDigitYearConverter,'yyyy')

app_name='shop'

urlpatterns=[
    path('archives/<yyyy:year>/', views.archives_year),
    path('items/', item_list, name='item_list'),
]