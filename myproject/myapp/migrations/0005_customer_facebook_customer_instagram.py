# Generated by Django 5.0.4 on 2024-08-03 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_menuitem_storeid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='facebook',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='instagram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
