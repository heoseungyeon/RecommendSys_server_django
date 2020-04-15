from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from place_detail import views

urlpatterns = [
    path('1/', views.CreatePlaceActivity.as_view()),
    path('2/', views.Pick_PlaceActivity.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)