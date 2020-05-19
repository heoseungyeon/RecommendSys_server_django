from django.urls import path, include
from . import views

urlpatterns = [
    # FBV
    path('text/recommend/', views.TextRecommendAPIView.as_view()),
    path('image/recommend/', views.ImageRecommendAPIView.as_view()),

]