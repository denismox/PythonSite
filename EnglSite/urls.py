from EnglSite import views
from django.urls import path

urlpatterns = [
    path("", views.hello, name='hello'),
    # path("dictonaty", views.dictonary, name = 'dictonary')
]