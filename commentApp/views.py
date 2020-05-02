from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import CommentsSerializer, PostingReviewSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import permissions
from knox.auth import TokenAuthentication
from rest_framework.renderers import JSONRenderer

# Create your views here.

class CommentListAPIView(APIView):
    # renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, posting_idx):
        place_history = UserPlaceHistory.objects.get(idx = posting_idx)
        # comments = PostingReviews.objects.filter(posting_idx = posting_idx)
        serializer = CommentsSerializer(place_history)
        return Response({

            "posting_reivew": serializer.data

        })

    def post(self, request):
        print(request.data)
        print(request.user)
        comment = PostingReviews.objects.create(user_idx = request.user)
        serializer = PostingReviewSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CommentDetailAPIView(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_object(self, idx):
        try:
            return PostingReviews.objects.get(idx=idx)
        except PostingReviews.DoesNotExist:
            raise Http404

    def get(self, request, idx, format=None):
        comment = self.get_object(idx)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, idx):
        comment = self.get_object(idx)
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, idx):
        post = self.get_object(idx)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)