from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets, permissions
from knox.auth import TokenAuthentication
from .service import *
from .object_size import *

# Create your views here.
class RecommendAPIView(APIView):

    authentication_classes = [TokenAuthentication,]
    permission_classes = [
        permissions.IsAuthenticated,
                          ]

    # def get(self, request, format=None):
    #
    #
    #     # opencb()
    #     return Response({
    #         "cb": 1
    #     })

    def post(self, request):

        query_set = getRecommend(request.data.get('request_sentence'), request.user)

        serializer = RecommendSerializer(query_set, many=True)
        print(serializer.data)
        print(type(serializer.data))
        return Response({
            "recommendation": serializer.data
        })

