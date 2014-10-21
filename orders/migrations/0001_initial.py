# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_name', models.CharField(max_length=200)),
                ('customer_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('customer_address', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('item_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('order_name', models.CharField(max_length=200)),
                ('order_cost', models.IntegerField()),
                ('cust_id', models.ForeignKey(to='orders.Customers')),
                ('item_id', models.ForeignKey(to='orders.Items')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('shipment_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('date_started', models.DateField()),
                ('date_arrived', models.DateField()),
                ('order_id', models.ForeignKey(to='orders.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
