from django.urls import path
from form import views

app_name='form'

urlpatterns = [path('',views.form_name_view,name="form"),]
