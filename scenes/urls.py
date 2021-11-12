"""
Urls for Scenes App
"""
from django.urls import path
from scenes import views

urlpatterns = [
    path('scenes/', views.ScenesList.as_view()),
    path('scenes/<int:pk>/', views.SceneDetail().as_view()),
]
