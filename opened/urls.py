from django.urls import path
from opened import views

urlpatterns = [
    path('opened/', views.OpenedList.as_view()),
    path('opened/<int:pk>/', views.OpenedDetail.as_view()),
    path('openedDept/', views.OpenedDeptList.as_view()),
    path('openedDept/<int:pk>/', views.OpenedDeptDetail.as_view()),
]
