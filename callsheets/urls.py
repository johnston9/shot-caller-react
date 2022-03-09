"""
Urls for Callsheet App
"""
from django.urls import path
from callsheets import views

urlpatterns = [
    path('crewinfo/', views.CrewInfoList.as_view()),
    path('crewinfo/<int:pk>/', views.CrewInfoDetail.as_view()),
    path('callsheets/', views.CallsheetList.as_view()),
    path('callsheets/<int:pk>/', views.CallsheetDetail.as_view()),
]
