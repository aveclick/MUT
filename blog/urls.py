from django.urls import path
from . import views
from .views import base, post_detail

urlpatterns = [
    path('', base, name='base'),
    path('<slug:slug>', post_detail, name='post_detail'),
]
