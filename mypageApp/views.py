from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import permissions
from knox.auth import TokenAuthentication
from .models import *

# Create your views here.
class MyPageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        serializer = MyPageSerializer(request.user)
        return Response({
           "my_page": serializer.data
        })

    def put(self, request, format=None):
        serializer = MyPageSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserPageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self, idx):
        try:
            return User.object.get(idx=idx)
        except User.DoesNotExist:
            raise Http404

    # def get_object_by_id(self, user_id):
    #     try:
    #         return User.object.get(user_id = user_id)
    #     except User.DoesNotExist:
    #         raise Http404

    def get(self, request, idx, format=None):
        user_page = self.get_object(idx)
        serializer = UserPageSerializer(user_page)
        # 포스팅 썸네일 = place_id 일단,,
        return Response({

            "user_page" : serializer.data
        })
