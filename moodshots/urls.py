""" Moodshots urls
    In Shot Caller DRF the work Mootshot is used throughout
    for the Moodboard App in Shot Caller React
"""
from django.urls import path
from moodshots import views

urlpatterns = [
    path('moodshots/', views.MoodshotList.as_view()),
    path('moodshots/<int:pk>/', views.MoodshotDetail.as_view()),
]
