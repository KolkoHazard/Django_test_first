from django.urls import path
from . import views

app_name = 'user_logout'

urlpatterns=[path('',views.user_logout,name='user_logout')]
