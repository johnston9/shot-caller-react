from django.urls import path
from departments import views

urlpatterns = [
    path('department/posts/', views.DepartmentList.as_view()),
    path('department/posts/<int:pk>/', views.DepartmentDetail.as_view()),
]
