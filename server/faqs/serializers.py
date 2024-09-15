from rest_framework import serializers
from .models import FruitFAQ

class FruitFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitFAQ
        fields = ['id', 'fruit_name', 'question', 'answer', 'created_at', 'updated_at']
