from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets, permissions
from knox.auth import TokenAuthentication
from .service import *
from rest_framework import status

# Create your views here.
class TextRecommendAPIView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
                          ]


    def post(self, request):
        query_set = getRecommend(request.data.get('recommend'), request.user)

        serializer = RecommendSerializer(query_set, many=True)
        print(serializer.data)
        print(type(serializer.data))
        return Response({
            "recommendation": serializer.data
        })

class ImageRecommendAPIView(APIView):

    permission_classes = [
        permissions.IsAuthenticated,
                          ]


    def post(self, request):

        upload_serializer = UploadSerializer(data = request.data)
        if upload_serializer.is_valid():
            upload_serializer.save()
            return Response({
                "recommendation": upload_serializer.data
            })

        return Response(upload_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

