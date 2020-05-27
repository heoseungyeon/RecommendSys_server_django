from rest_framework import serializers
# from .models import UserPick
from recommendApp.models import *
from pick.models import UserPick


class RecommendUserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = ['place_id', 'place_name']

class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = '__all__'


class PickPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPick
        fields = '__all__'


class CategoryImageMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImageM
        fields = '__all__'


class CategoryImageSSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryImageS
        fields = '__all__'


class HomeSerializer(serializers.ModelSerializer) :

    recommend_place = RecommendUserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'nickname', 'recommend_place')