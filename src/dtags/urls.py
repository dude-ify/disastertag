"""dtags URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.Landing.index, name='index'),
    path('add/', views.Create.index, name='create'),
    path('read/', views.Read.index, name='read'),
    path('read/<int:patient_id>/', views.Read.info, name='info'),
    path('delete/<int:pk>/', views.DtagDelete.as_view(), name='del_item')
]

urlpatterns += staticfiles_urlpatterns()
