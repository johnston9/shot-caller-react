from django.urls import path
from archives import views

urlpatterns = [
    path('archives/', views.ArchiveList.as_view()),
    path('archives/<int:pk>/', views.ArchiveDetail.as_view()),
]
