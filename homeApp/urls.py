from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeListAPIView.as_view()),
    path('search/', views.SearchListAPIView.as_view()),

]