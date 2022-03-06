"""
Urls for Callsheet App
"""
from django.urls import path
from callsheets import views

urlpatterns = [
    path('callsheets/', views.CrewInfoList.as_view()),
    path('callsheets/<int:pk>/', views.CrewInfoDetail.as_view()),
]
