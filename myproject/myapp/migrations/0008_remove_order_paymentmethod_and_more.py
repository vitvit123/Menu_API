# Generated by Django 5.0.4 on 2024-08-18 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_order_storeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paymentmethod',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paymentresult',
        ),
    ]
