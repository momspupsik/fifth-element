from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('plk', views.plk),
    path('upload', views.upload)
]
