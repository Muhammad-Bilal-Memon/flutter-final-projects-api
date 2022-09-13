from rest_framework import serializers
from .models import allData


class allDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = allData
        fields = ["title", "price", "created_by", "description"]
