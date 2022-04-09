from django.urls import path

from django.urls import re_path
from .views import *

app_name = 'store'
urlpatterns = [
    path('store/', ProductList.as_view(), name='store'),
    path('detail/<int:id>/', product_detail, name='product_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]