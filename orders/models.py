from django.db import models

# Create your models here.

#class Items(models.Model):
#    item_id = models.CharField(max_length=200,primary_key=True)
#    item_name = models.CharField(max_length=200)

#class Customers(models.Model):
#    customer_name = models.CharField(max_length=200)
#    customer_id = models.CharField(max_length=200,primary_key=True)
#    customer_address = models.CharField(max_length=200)

#class Shipment(models.Model):
#    shipment_id = models.CharField(max_length=200, primary_key=True)
#    order_id = models.ForeignKey(Order, to_field='order_id')
#    date_started = models.DateField()
#    date_arrived = models.DateField()
from customers.models import Customers
from items.models import Items
import uuid

class Order(models.Model):
    order_id = models.CharField(max_length=200, primary_key=True)
    item_id = models.ForeignKey(Items,to_field='item_id')
    #order_name = models.CharField(max_length=200)
    order_cost = models.IntegerField()
    number_of_items = models.IntegerField()
    cust_id = models.ForeignKey(Customers, to_field='customer_id')

    def generate_order_id(self):
        return uuid.uuid4()

    def generate_order_name(self):
        pass

    def get_customer_id(self):
        pass

    def get_item_cost(self):
        pass


    def remove_order(self, item_id, number_of_items):
        self.update_order(item_id, number_of_items=number_of_items)


    def get_order_details(self, valid_order_id):

        pass

    def compare_order(self, order_a, order_b, class_name):
        pass

    def update_order(self, item_id, number_of_items):
        self.place_order(item_id, updating_current_order=True)

    def check_order_placed(self, order_id, order_to_be_checked=None):
        order_placed = Order.objects.filter(order_id=order_id)
        self.compare_order(order_placed, order_to_be_checked, Order)

    def place_order_for_list_of_item(self, dict_with_item_quantiy):
        order_uuid = self.generate_order_id()
        for item_id, quantity in dict_with_item_quantiy.iteritems():
            self.place_order(item_id,number_of_items=quantity, order_id=order_uuid)

    def place_order(self, item_id, number_of_items=1, order_name=None,order_id=None,updating_current_order=False):
        if order_id is None:
            order_id=self.generate_order_id()
        if item_cost
        item_cost = self.get_item_cost()
        new_order = Order(order_id = order_id, item_id= item_id, order_cost = '', cust_id= '')
        order_to_checked = new_order
        new_order.save()
