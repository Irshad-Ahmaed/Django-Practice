from django.urls import path
from . import views

urlpatterns = [
    path('', views.htmlHome, name='htmlHome'),
    path('chai/', views.get_chai, name='get_chai'),
]