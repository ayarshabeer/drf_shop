from __future__ import unicode_literals
from rest_framework import serializers
from carts.models import Cart, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item


class CartSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        item_queryset = Item.objects.filter(cart_id=obj.id)
        serializer = ItemSerializer(instance=item_queryset, many=True)
        return serializer.data

    class Meta:
        model = Cart