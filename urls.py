from django.contrib import admin
from django.urls import path 

from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path ('contact/', contact, name='contact'),
    path('admin/', admin.site.urls), 
]

"""taskmanager URL Configuration 

The 'urlpatterns' list routes URLs to views. For Information please see:
  http://docs.djangoproject.com/en/3.0/topics/urls/
Examples:
Function views 
  1. Add an import: from my_app import views
  2. Add a URL urlpatterns: path('', views.home, name='home')
Class-based views
  1. Add an import: from_other_app.views import Home
  2. Add a URL to urlpatterns: path('', Home.as_views(), name='home')
Including another conf
  1. Import the include() function: from django.urls import include, path 
  2. Add a URL to urlpatterns: path('blog/, include(blog.urls))
"""
Import ...

urlpatterns = [
  path('admin/', admin.site.urls),
]




