from django.urls import path, include
from . import views

urlpatterns = [
    # FBV
    path('recommend/', views.RecommendAPIView.as_view()),

]