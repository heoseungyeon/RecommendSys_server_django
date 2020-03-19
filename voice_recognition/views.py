from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post
from .models import *

from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from konlpy.tag import Komoran
from rest_framework.request import Request
from rest_framework import permissions
from ast import literal_eval
# Create your views here.
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "voice_recognition.settings")


class PostList(APIView):
    renderer_classes = [JSONRenderer]

    # 게시물 생성
    def post(self, request, fromat=None):
        print("data:",request.data)
        print(type(request.data))
        komoran = Komoran()

        analysis = komoran.morphs(request.data.get('content'))
        print(analysis)
        for ctgr in CategoryS.objects.all():
            for morph in analysis:
                if ctgr.ctgr_name == morph:
                    print("카테고리 소항목이 있습니다: ",ctgr.ctgr_name)
        string1="{'content':'"
        string2="'}"
        analysis=string1+','.join(analysis)+string2
        print(analysis)
        analysisdic=literal_eval(analysis)
        serializer = PostSerializer(data=analysisdic)
        #serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 게시물 조회
    def get(self, request, format=None):
        queryset = Post.objects.all()

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get_object(selfself, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    # 특정 게시물 조회 /post/{pk}/
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # 특정 게시물 수정 /post/{pk}/
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 특정 게시물 삭제 /post/{pk}/
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
