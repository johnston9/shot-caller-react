from django.urls import path
from indexshots1 import views

urlpatterns = [
    path('series/', views.SeriesList.as_view()),
    path('series/<int:pk>/', views.SeriesDetail.as_view()),
    path('indexshots/', views.IndexShotList.as_view()),
    path('indexshots/<int:pk>/', views.IndexShotDetail.as_view())
]
