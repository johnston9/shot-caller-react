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
    path('castcalls/', views.CastcallList.as_view()),
    path('castcalls/<int:pk>/', views.CastcallDetail.as_view()),
    path('backgroundcalls/', views.BackgroundcallList.as_view()),
    path('backgroundcalls/<int:pk>/', views.BackgroundcallDetail.as_view()),
]
