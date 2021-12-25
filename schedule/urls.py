"""
Urls for Schedule App
"""
from django.urls import path
from schedule import views

urlpatterns = [
    path('days/', views.DayList.as_view()),
    path('days/<int:pk>/', views.DayDetail().as_view()),
]
