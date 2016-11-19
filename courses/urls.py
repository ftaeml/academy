from django.conf.urls import url
from django.contrib import admin
from courses import views

urlpatterns = [
    url(r'^courses/', views.cours),
]
