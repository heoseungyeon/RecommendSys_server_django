from  rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from follow_feed.models import *

from rest_framework.renderers import JSONRenderer

from follow_feed.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
import json

#CreateFeedActivity
class CreateFeedActivity(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        userplacehistory = UserPlaceHistory.objects.all()
        serializer = UserPlaceHistorySerializer(userplacehistory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_id = request.user.idx
        print("user_id:",user_id)
        #queryset 생성
        user_follow = UserFollow.objects.all()
        userplacehistory = UserPlaceHistory.objects.all().order_by('-date')
        #유저의 팔로잉 유저 리스트
        follow_list= []
        #유저의 팔로잉 유저 찾기
        for follow in user_follow:
            if follow.user_idx.idx == int(user_id):
                follow_list.append(follow.following_idx.idx)

        print(follow_list)

        #클라이언트에 보낼 데이터 리스트
        data= []
        #유저의 팔로잉 유저의 게시물 찾기
        for place in userplacehistory:
            print(place.user_idx.idx)
            if place.user_idx.idx in follow_list:
                print("place: ",place)
                temp = dict()
                temp["posting_id"] = place.idx
                temp["user_idx"] = place.user_idx.idx #외래키 이므로 해당 값을 갖는 user 테이블의 값을 한번 더 참조해야함
                temp["place_id"] = place.place_id
                temp["context"] = place.context
                if place.img_url_1:
                    temp["img_url_1"] = place.img_url_1.url
                else:
                    print("url_1 없네요")
                if place.img_url_2:
                    temp["img_url_2"] = place.img_url_2.url
                else:
                    print("url_2 없네요")
                if place.img_url_3:
                    temp["img_url_3"] = place.img_url_3.url
                else:
                    print("url_2 없네요")
                if place.img_url_4:
                    temp["img_url_4"] = place.img_url_4.url
                else:
                    print("url_4 없네요")
                if place.img_url_5:
                    temp["img_url_5"] = place.img_url_5.url
                else:
                    print("url_5 없네요")
                temp["like_cnt"] = place.like_cnt
                temp["date"] = place.date
                temp["tag_1"] = place.tag_1
                temp["tag_2"] = place.tag_2
                temp["tag_3"] = place.tag_3
                temp["tag_4"] = place.tag_4
                temp["tag_5"] = place.tag_5
                temp["tag_6"] = place.tag_6
                temp["rating"] = place.rating
                data.append(temp)
        #팔로잉 유저 리스트 response 에 담기
        temp=dict()
        temp["follow_list"] = follow_list
        data.append(temp)
        print("data: ", data)


        return Response(data, status=status.HTTP_201_CREATED)
        #return Response(data, status=status.HTTP_400_BAD_REQUEST)

#LikeViews
class LikeViews(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        userplacehistory = UserPlaceHistory.objects.all()
        serializer = UserPlaceHistorySerializer(userplacehistory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user_id= request.user.idx
        posting_id = request.data.get('posting_id')
        #userlikehistory queryset 생성
        userlike = UserLikeHistory.objects
        #request 값으로 필터링
        instance = userlike.filter(user_idx=int(user_id), posting_idx=int(posting_id))
        #유효정보 저장
        valid = instance.exists()
        print(valid)
        # result 반환 정보 입력
        result = dict()
        result["valid"] = valid
        # DB 정보 data 입력
        data = dict()
        data["user_idx"] = int(user_id)
        data["posting_idx"] = int(posting_id)
        print(data)
        if valid == False:
            serializer = UserLikeHistorySerializer(data=data)
            if serializer.is_valid():
                print("valid")
                serializer.save()
                #user_place_history 해당 포스팅 좋아요 갯수 +1
                posting = UserPlaceHistory.objects.get(idx=posting_id)
                posting.like_cnt=posting.like_cnt+1
                posting.save()
            else:
                print("bad")
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        if valid == True:
            instance.delete()
            # user_place_history 해당 포스팅 좋아요 갯수 -1
            posting = UserPlaceHistory.objects.get(idx=posting_id)
            posting.like_cnt = posting.like_cnt - 1
            posting.save()

        return Response(result, status=status.HTTP_201_CREATED)



#ReviewViews
class ReviewViews(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        userplacehistory = UserPlaceHistory.objects.all()
        serializer = UserPlaceHistorySerializer(userplacehistory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # 클라이언트에 보낼 데이터 리스트
        data = []
        posting_id= request.data.get('posting_id')
        #queryset 생성
        posting_reviews = PostingReviews.objects.all().order_by('-date')
        #해당 게시글 posting_Review 찾기
        for review in posting_reviews:
            print(review.posting_idx)
            print(posting_id,"ddd")
            if review.posting_idx.idx == int(posting_id):
                temp = dict()
                temp["user_idx"] = review.user_idx.idx
                temp["context"] = review.context
                temp["date"] = review.date
                data.append(temp)

        #데이터 출력해보기
        print("data: ", data)


        return Response(data, status=status.HTTP_201_CREATED)
        #return Response(data, status=status.HTTP_400_BAD_REQUEST)

