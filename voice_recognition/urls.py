from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
urlpatterns = [
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]