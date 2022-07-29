"""
Urls for Script App
"""
from django.urls import path
from script import views

urlpatterns = [
    path('script/', views.ScriptList.as_view()),
    path('script/<int:pk>/', views.ScriptDetail.as_view()),
]
