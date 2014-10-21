from django.db import models


class Items(models.Model):
    item_id = models.CharField(max_length=200,primary_key=True)
    item_name = models.CharField(max_length=200)
