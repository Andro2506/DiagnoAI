from django.contrib import admin
from django.urls import path, include
from .views import predict, history, getdoctor

urlpatterns = [
    path('predict/', predict, name='predict'),
    path('history/', history, name='history'),
    path('getdoctor/', getdoctor, name='getdoctor'),
]