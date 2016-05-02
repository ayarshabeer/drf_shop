from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault, CreateOnlyDefault
from products.models import Manufacturer, Category, Product, ProductImage


class ManufacturerSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=CreateOnlyDefault(CurrentUserDefault())
    )

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=CreateOnlyDefault(CurrentUserDefault())
    )

    class Meta:
        model = Category
        fields = ('id', 'title', 'slug', 'description', 'is_featured')


class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=CreateOnlyDefault(CurrentUserDefault())
    )

    class Meta:
        model = Product


class ProductImageSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(
        default=CreateOnlyDefault(CurrentUserDefault())
    )

    class Meta:
        model = ProductImage
