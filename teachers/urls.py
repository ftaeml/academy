from django.conf.urls import url
from django.contrib import admin
from teachers import views

urlpatterns = [
    url(r'^teachers/', views.teacher),
]
