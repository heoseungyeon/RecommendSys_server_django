from rest_framework import serializers
from loginApp.serializers import UserSerializer
from .models import *
from django.db.models import Avg, Max, Min, Sum

class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = ('place_id', )


class RecommendSerializer(serializers.ModelSerializer) :

    place = UserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'nickname', 'place')

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields = '__all__'