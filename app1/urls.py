from django.urls import path
from .views import *

app_name = 'app1'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/<int:pk>', AboutView.as_view(), name='about'),
    path('request/', RequestView.as_view(), name='request'),
]

