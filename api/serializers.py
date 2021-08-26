
from rest_framework import serializers
from .models import history, user, RefCode

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields = '__all__'
        extra_kwargs = {
            "password": {'write_only': True}
        }

class RefCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=RefCode
        fields='__all__'

class historySerializer(serializers.ModelSerializer):
    class Meta:
        model=history
        fields='__all__'
       