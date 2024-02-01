from django.db import models

# Create your models here.
class products(models.Model):
     image=models.ImageField(upload_to='images')
     name=models.CharField(max_length=50)
     price=models.IntegerField()

     def __str__(self):
         return self.name
