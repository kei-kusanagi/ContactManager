from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)

class Contact(models.Model):
    category = models.ForeignKey(Category, related_name='contacts', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    lasst_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)