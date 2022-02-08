from django.db import models

# Create your models here.
from django.db import models


class Home(models.Model):
    
    description = models.TextField(max_length=1000)
    price = models.CharField(max_length=10)
    Category=models.ForeignKey("Category", on_delete=models.CASCADE)
    code=models.CharField( max_length=50)
    
    
    
    def __str__(self):
        return self.description
class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name
    
    