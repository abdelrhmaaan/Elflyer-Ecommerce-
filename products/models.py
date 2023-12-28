from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=40,default='')
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE,default=1,null=True)
    price = models.DecimalField(default=22,max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='')
    desc = models.TextField(default='Test discription')
    stock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40,default='Test')
    image = models.ImageField(upload_to='')
    desc= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self) -> str:
        return self.name
