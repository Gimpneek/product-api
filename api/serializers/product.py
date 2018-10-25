"""
Serializer for Product model
"""
from rest_framework import serializers
from api.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product
    """

    class Meta:
        """
        Definition of the serializer
        """
        model = Product
        fields = (
            'id',
            'name',
            'price'
        )
