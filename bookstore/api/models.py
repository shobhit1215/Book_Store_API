from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Book(models.Model):
    title=models.CharField(max_length=150)
    category=models.ForeignKey(Category,related_name='books',on_delete=models.CASCADE)
    pages=models.IntegerField()
    price=models.IntegerField()
    author=models.CharField(max_length=50)
    contact=models.IntegerField()
    payment=models.CharField(max_length=50)

    def __str__(self):
        return self.title