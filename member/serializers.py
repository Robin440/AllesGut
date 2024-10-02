from rest_framework import serializers
from accounts.serializer import UserSerializer

from member.models import Member,MemberImage

class MemberImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberImage
        exclude=['uuid']

class MemberImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberImage
        fields = '__all__'


class MemberCreateSerializers(serializers.ModelSerializer):
  
    class Meta:
        model = Member
        exclude=['uuid']
    
class MemberListSerializers(serializers.ModelSerializer):
    user = UserSerializer()  # Nested user details
    member_image = MemberImageListSerializer(many=True, source='memberimage_set')  # Nested images

    class Meta:
        model = Member
        fields = '__all__'


