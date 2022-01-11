
from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=200)
    isbn=models.CharField(max_length=14)
    country=models.CharField(max_length=200)
    number_of_pages=models.IntegerField()
    publisher=models.CharField(max_length=200)
    release_date=models.DateField(default='1999-11-11')
    authors=models.CharField(max_length=300)
class Author(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name