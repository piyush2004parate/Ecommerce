# Generated by Django 3.2.25 on 2024-07-08 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
    ]