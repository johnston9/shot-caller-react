from django.urls import path
from indexshots1 import views

urlpatterns = [
    path('indexshot1/', views.IndexShot1List.as_view()),
    path('indexshot1/<int:pk>/', views.IndexShot1Detail.as_view())
]
