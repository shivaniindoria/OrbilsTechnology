from rest_framework import serializers
from .models import CartItem

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['id', 'name']