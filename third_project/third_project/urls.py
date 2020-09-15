"""third_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from index import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',include('contact.urls')),
    path('form/',include('form.urls')),
    path('form2/',include('form2.urls')),
    path('registration/',include('registration.urls')),
    path('user_login/',include('user_login.urls')),
    path('logout/',include('user_logout.urls')),
    path('special/',include('special.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
