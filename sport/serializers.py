from rest_framework import serializers
from sport.models import sportitem, sportrecord

class SportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = sportitem
        fields ='__all__'

class SportRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = sportrecord
        fields ='__all__'