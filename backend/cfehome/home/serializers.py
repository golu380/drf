from rest_framework import serializers
from .models import Person,Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields = ['color_name','id']
        

class  PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    color_info = serializers.SerializerMethodField()
    class Meta:
        model = Person
        fields = '__all__'
        # depth = 1
    
    def get_color_info(self,obj):
        color_obj = Color.objects.get(id = obj.color.id)
        
        return {'color_name':color_obj.color_name,'hex_code':'#000'}
    
        
    def validate(slef,data):
        spacial_character = "!@#$%^&*()_+=?_,<>/"
        if any(c in spacial_character for c in data['name']):
            raise serializers.ValidationError('name can not contain spacial chars')
        if data['age'] <18:
            raise  serializers.ValidationError('Age should be greater than 18')
        return data