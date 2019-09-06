"""knight URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from crm import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'login/', views.Login_view.as_view(), name='login'),
    url(r'register/', views.Register.as_view(), name='register'),
    url(r'index/', views.index, name='index'),
    url(r'check_paaword/', views.check_paaword, name='check_paaword'),
    url(r'check_email/', views.check_email, name='check_email'),

    url(r'crm/',include('crm.crm_urls'))
]
