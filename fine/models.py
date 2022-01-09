from django.db import models

# Create your models here.

class member(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=19)
    phn=models.IntegerField(default='')
    email=models.EmailField(default='')
    def __str__(self):
        return self.username

class Books(models.Model):
    bookname=models.CharField(max_length=30)
    discription=models.CharField(max_length=50)
    price=models.IntegerField(default='')
    def __str__(self):
        return self.bookname

class pro(models.Model):
    name = models.CharField(max_length=100)
    prod = models.CharField(max_length=100)
    des = models.TextField(max_length=100)
    price=models.IntegerField(default='')
    def __str__(self):
        return self.name