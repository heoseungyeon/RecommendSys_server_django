from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets, permissions
from knox.auth import TokenAuthentication
from .service import get_random_m, get_random_s, get_home_recommend
from .models import *


# Create your views here.

class HomeListAPIView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):

        user = request.user
        query_set = get_home_recommend(user)
        home_serializer = HomeSerializer(query_set, many= True)

        user_pick = user.home_userpick_set.all()
        pick_serializer = PickPlaceSerializer(user_pick, many=True)


        realtime_reviews = UserPlaceHistory.objects.all().order_by('-date')[:8]
        real_serializer = UserPlaceHistorySerializer(realtime_reviews, many=True)

        hot_reviews = UserPlaceHistory.objects.all().order_by('-like_cnt')[:8]
        hot_serializer = UserPlaceHistorySerializer(hot_reviews, many=True)

        category_m = get_random_m()
        category_m_serializer = CategoryImageMSerializer(category_m, many=True)

        category_s = get_random_s()
        category_s_serializer = CategoryImageSSerializer(category_s, many= True)


        return Response({
            "home_recommendation":home_serializer.data,
            "user_pick" : pick_serializer.data,
            "real_time": real_serializer.data,
            "hot": hot_serializer.data,
            "category_m": category_m_serializer.data,
            "category_s": category_s_serializer.data

        })

class SearchListAPIView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):

        # user = request.user
        # query_set = get_home_recommend(user)
        # home_serializer = HomeSerializer(query_set, many= True)

        # user_pick = user.userpick_set.all()
        # pick_serializer = PickPlaceSerializer(user_pick, many=True)

        realtime_reviews = UserPlaceHistory.objects.all().order_by('-date')[:8]
        real_serializer = UserPlaceHistorySerializer(realtime_reviews, many=True)

        hot_reviews = UserPlaceHistory.objects.all().order_by('-like_cnt')[:8]
        hot_serializer = UserPlaceHistorySerializer(hot_reviews, many=True)

        category_m = get_random_m()
        category_m_serializer = CategoryImageMSerializer(category_m, many=True)

        category_s = get_random_s()
        category_s_serializer = CategoryImageSSerializer(category_s, many= True)


        return Response({

            # "home_recommendation":home_serializer.data,
            # "user_pick" : pick_serializer.data,
            "realtime_posting": real_serializer.data,
            "hot_posting": hot_serializer.data,
            "category_m": category_m_serializer.data,
            "category_s": category_s_serializer.data

        })