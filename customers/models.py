from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_id = models.CharField(max_length=200,primary_key=True)
    customer_address = models.CharField(max_length=200)
