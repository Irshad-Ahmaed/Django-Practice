from django.urls import path
from . import views

urlpatterns = [
    path('', views.htmlHome, name='htmlHome'),
    path('chai/', views.get_chai, name='get_chai'),
    path('chai/<int:chai_id>/', views.chai_detail, name='chai_detail'),
]