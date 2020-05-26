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

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):

        print(request.data)
        serializer = MyPageSerializer(request.user)
        return Response({
           "mypage": serializer.data
        })

    def put(self, request, format=None):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mypage":serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):

        request.user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserPageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self, nickname):
        try:
            return User.object.get(nickname=nickname)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, nickname, format=None):
        user_page = self.get_object(nickname)
        serializer = UserPageSerializer(user_page)

        # 포스팅 썸네일 = place_id 일단,, 이거 바꿔야함 image필드로
        return Response({

            "userpage" : serializer.data
        })
