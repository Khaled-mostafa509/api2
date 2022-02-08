from rest_framework import serializers
from .models import Home , Category

class HomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        
class CategorySerializers(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'