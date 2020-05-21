from  rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from posting.models import *
from rest_framework.renderers import JSONRenderer

from posting.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from posting.services import *
import json

#UpLoadPosting
class UpLoadPosting(APIView):
    renderer_classes = [JSONRenderer]

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #Request값 받기
        user_id= request.user.idx
        #posting_cnt +1
        userPostCnt(user_id)

        #export to deepLearning Module
        post_id = currentPostId()+1
        print(post_id)#test
        #imageScore=AnalyzeImage(post_id)
        #textSocre=AnalyzeText(post_id)
        imageScore = dict()
        textScore = dict()

        #테스트 
        imageScore['칼국수']=1
        textScore['매콤한']=1
        #Insert to UserPlaceHistory
        check=insertUserPlaceHistory(request,post_id)

        #Insert to Score
        if check==True:
            insertScore(request, imageScore, textScore)

        data= []
        temp=dict()
        temp['check']=check
        data.append(temp)

        return Response(data, status=status.HTTP_201_CREATED)

