
from place_detail.models import UserPlaceHistory
from place_detail.models import UserPick
from rest_framework.renderers import JSONRenderer

from place_detail.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

#CreatePlaceActivity
class CreatePlaceActivity(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        userplacehistory = UserPlaceHistory.objects.all()
        serializer = UserPlaceHistorySerializer(userplacehistory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        place_id= request.data.get('place_id')
        rating=0.0
        userplacehistory = UserPlaceHistory.objects.all()
        data= []
        for place in userplacehistory:
            if place.place_id == place_id:
                print(place)
                temp = dict()
                temp["posting_id"] = place.idx
                temp["user_idx"] = place.user_idx.idx #외래키 이므로 해당 값을 갖는 user 테이블의 값을 한번 더 참조해야함
                temp["place_id"] = place.place_id
                temp["context"] = place.context
                temp["img_cnt"] = place.img_cnt
                rating = rating + float(place.rating)
                data.append(temp)
                print(data)
        #serializer = UserPlaceHistorySerializer(data=request.data)
        #if serializer.is_valid():
        temp = dict()
        temp["rating"] = rating
        data.append(temp)
        return Response(data, status=status.HTTP_201_CREATED)
        #return Response(data, status=status.HTTP_400_BAD_REQUEST)


#Pick_PlaceActivity(APIView)
class Pick_PlaceActivity(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        userpick = UserPick.objects.all()
        serializer = UserPickSerializer(userpick, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        user_id = request.data.get('user_id')
        place_id = request.data.get('place_id')
        print(type(user_id))
        print(type(place_id))

        userpick = UserPick.objects
        instance = userpick.filter(user_idx=int(user_id),place_id=place_id)

        valid = instance.exists()
        print(valid)
        #result 반환 정보 입력
        result= dict()
        result["valid"]=valid
        #DB 정보 data 입력
        data = dict()
        data["user_idx"]=int(user_id)
        data["place_id"]=place_id
        print(data)
        if valid == False:
            serializer = UserPickSerializer(data=data)
            if serializer.is_valid():
                print("valid")
                serializer.save()
            else :
                print("bad")
                return Response(result, status=status.HTTP_400_BAD_REQUEST)

        if valid == True:
            instance.delete()

        return Response(result, status=status.HTTP_201_CREATED)



#UserPlaceHistory table
class UserPlaceHistoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        userplacehistory = UserPlaceHistory.objects.all()
        serializer = UserPlaceHistorySerializer(userplacehistory, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserPlaceHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPlaceHistoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserPlaceHistory.objects.get(pk=pk)
        except UserPlaceHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userplacehistory = self.get_object(pk)
        serializer = UserPlaceHistorySerializer(userplacehistory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userplacehistory = self.get_object(pk)
        serializer = UserPlaceHistorySerializer(userplacehistory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userplacehistory = self.get_object(pk)
        userplacehistory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#user_pick 테이블
class UserPickList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        userpick = UserPlaceHistory.objects.all()
        serializer = UserPlaceHistorySerializer(userpick, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserPickSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPickDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UserPick.objects.get(pk=pk)
        except UserPlaceHistory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        userpick = self.get_object(pk)
        serializer = UserPlaceHistorySerializer(userpick)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        userpick = self.get_object(pk)
        serializer = UserPlaceHistorySerializer(userpick, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        userpick = self.get_object(pk)
        userpick.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)