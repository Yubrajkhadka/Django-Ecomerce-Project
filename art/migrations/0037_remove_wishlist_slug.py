# Generated by Django 4.1.1 on 2023-03-01 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0036_alter_order_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='slug',
        ),
    ]
