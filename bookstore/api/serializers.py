from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title')
        model=Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','title','category','pages','price','author','contact','payment')
        model=Book