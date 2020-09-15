from django.urls import path
from . import views

app_name = 'special'

urlpatterns=[path('',views.special,name='special')]
