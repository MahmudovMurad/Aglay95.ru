from django.urls import path
from unicodedata import name

from django.urls import re_path
from .views import *
from core.views import *

# from django.conf.urls import  url



urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('subscribe/', SubscribeAPIView.as_view(), name="subscribe"),
    path('blog/', BlogList.as_view(), name='blog'),

]