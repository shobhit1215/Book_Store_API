from django.contrib import admin
from django.urls import path,include
from .views import * 
urlpatterns=[
    path('books',ListBook.as_view(),name='book'),
    path('books/<int:pk>/',DetailBook.as_view(),name='detailbook'),
    path('categories',ListCategory.as_view(),name='category'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='detailcategory'),

]