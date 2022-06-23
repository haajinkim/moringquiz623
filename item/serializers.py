from rest_framework import serializers
from .models import Category, Item, Order, ItemOrder



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["name","category","image_url"]

class CaregorySerializer(serializers.ModelSerializer):
    item_set = ItemSerializer(many=True)
    def get_items(self,obj):

        return "test"
    class Meta:
        model = Category
        fields = ["name","item_set"]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["delivery_address","order_date","item"]


class ItemOrderSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    class Meta:
        model = ItemOrder
        fields = ["order","item","item_count","itemOrder"]