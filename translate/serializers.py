from re import I
from rest_framework import serializers
from .models import Input

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = "__all__"