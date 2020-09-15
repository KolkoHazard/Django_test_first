from django.urls import path
from form2 import views

app_name='form2'

urlpatterns=[
    path('',views.form_name_view,name="form2"),
]
