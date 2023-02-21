# serializers.py
from rest_framework import serializers
from .models import OptionItem

class OptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionItem
        fields = '__all__'
