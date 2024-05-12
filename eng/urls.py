"""eng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from EnglSite import views

urlpatterns = [
    path("", views.for_base, name='for_base.html'),
    path("admin/", admin.site.urls),
    path("write_word", views.write_word, name="write_word.html"),
    path("dictonary", views.dictonary, name='dictonary.html'),
    path("send_word", views.send_word),
    path('delete_word', views.delete_word),
    path('update_word', views.update_word),
    path('check', views.check),
    path('send_check', views.send_check),

    
    # path('', views.hello, name='hello')
]
