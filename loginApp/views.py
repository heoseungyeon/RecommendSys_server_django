from django.shortcuts import render
from rest_framework import permissions, generics, status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from knox.models import AuthToken
from .serializers import *
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import TokenAuthentication
from django.contrib.auth import login


# Create your views here.
@api_view(["GET"])
def HelloAPI(request):

    print(request.user)
    return Response("hello world!")


class RegistrationAPI(generics.GenericAPIView):
    renderer_classes = [JSONRenderer]

    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data["user_id"]) < 6 or len(request.data["password"]) < 4:
            body = {"message": "short field"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


class LoginAPI(generics.GenericAPIView):
    renderer_classes = [JSONRenderer]
    # 토큰인증은 username, password로 로그인 인증을 하는데
    # username : 가입 시 name 이므로 email 주소이다.. 씨발;
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            "user": UserSerializer(user,
                                   context=self.get_serializer_context()).data['user_id'],
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = UserSerializer

    def get_object(self):
        print(self.request.auth)
        print(self.request.data)
        print(self.request.user.idx)
        print(self.request.content_type)
        print(self.request.FILES)
        print(self.request.user.user_email)
        print(self.request.user.idx)
        print(self.request.user.user_id)

        return self.request.user
