from rest_framework import serializers
# from .models import UserPick
from recommendApp.models import *
from pick.models import UserPick


class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = ('user_idx', 'place_id')


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

    place = UserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'user_id', 'place')