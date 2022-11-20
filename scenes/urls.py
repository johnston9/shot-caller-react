"""
Urls for Scenes App
"""
from django.urls import path
from scenes import views

urlpatterns = [
    path('scenes/', views.ScenesList.as_view()),
    path('scenes/<int:pk>/', views.SceneDetail.as_view()),
    path('scenecharacters/', views.SceneCharacterAddList.as_view()),
    path('scenecharacters/<int:pk>/', views.SceneCharacterAddDetail.as_view()),
]
