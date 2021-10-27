from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer,BookSerializer
from .models import Category,Book
# Create your views here.
class ListBook(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class ListCategory(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
