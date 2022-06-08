from django.urls import path
from indexcards import views

urlpatterns = [
    path('indexcards/', views.IndexCardList.as_view()),
    path('indexcards/<int:pk>/', views.IndexCardDetail.as_view())
]
