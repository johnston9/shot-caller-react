"""
Urls for Callsheetnew App new
"""
from django.urls import path
from callsheetsnew import views

urlpatterns = [
    path('crewinfonew/', views.CrewInfonewList.as_view()),
    path('crewinfonew/<int:pk>/', views.CrewInfonewDetail.as_view()),
    path('callsheetsnew/', views.CallsheetnewList.as_view()),
    path('callsheetsnew/<int:pk>/', views.CallsheetnewDetail.as_view()),
    path('castcallsnew/', views.CastcallnewList.as_view()),
    path('castcallsnew/<int:pk>/', views.CastcallnewDetail.as_view()),
    path('backgroundcallsnew/', views.BackgroundcallnewList.as_view()),
    path('backgroundcallsnew/<int:pk>/', views.BackgroundcallnewDetail.as_view()),
    path('extracrewinfo/', views.ExtraCrewInfoList.as_view()),
    path('extracrewinfo/<int:pk>/', views.ExtraCrewInfoDetail.as_view()),
]
