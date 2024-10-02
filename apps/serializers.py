from rest_framework import serializers
from app.models import App

class  AppCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=App
        exclude = ['uuid']


class  AppListSerializer(serializers.ModelSerializer):
    class Meta:
        model=App
        fields='__all__'  # '__all__' 表示序列化所有字段