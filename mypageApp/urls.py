from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('mypage/', views.MyPageDetail.as_view()),
    # path('userpage/', views.UserPageDetail.as_view()),
    path('userpage/<str:nickname>/', views.UserPageDetail.as_view()),
]
