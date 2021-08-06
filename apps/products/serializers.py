from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandVariant
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username', read_only=False)
    color_type = ColorSerializer()
    brand_type = BrandSerializer()
    size_type = SizeSerializer()

    class Meta:
        fields = '__all__'
        model = Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category
