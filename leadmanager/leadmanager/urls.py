from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('lead.urls')),
    path('test', include('testapp.urls')),
]
