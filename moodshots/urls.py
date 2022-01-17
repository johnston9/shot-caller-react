from django.urls import path
from moodshots import views

urlpatterns = [
    path('moodshots/', views.MoodshotList.as_view()),
    path('moodshots/<int:pk>/', views.MoodshotDetail.as_view()),
]
