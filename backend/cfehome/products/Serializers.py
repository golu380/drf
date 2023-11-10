from django import forms
from rest_framework import serializers

from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        # fields = '__all__'
        # fields = ('id','title','content','price','sale_price','get_discount')
        fields=[
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]
    def get_my_discount(self,obj):
        try:
            return obj.get_discount
        except:
            return None