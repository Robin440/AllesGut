from rest_framework import serializers

from my_ip.models import MyIP




class MyIPCreateSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = MyIP
        exclude = ['uuid']


class MyIPListSerializers(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = MyIP
        fields = '__all__'


    