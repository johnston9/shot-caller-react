"""
Urls for Shotlist App
"""
from django.urls import path
from shotlists import views

urlpatterns = [
    path('shotlists/', views.ShotlistList.as_view()),
    path('shotlists/<int:pk>/', views.ShotlistDetail.as_view())
]
