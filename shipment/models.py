from cloudkeep.barbican.orders.models.order import Order
from django.db import models

class Shipment(models.Model):
    shipment_id = models.CharField(max_length=200, primary_key=True)
    order_id = models.ForeignKey(Order, to_field='order_id')
    date_started = models.DateField()
    date_arrived = models.DateField()
# Create your models here.
