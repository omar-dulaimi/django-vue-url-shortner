from rest_framework import serializers
from .models import UserUrl


class UserUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUrl
        fields = '__all__'
