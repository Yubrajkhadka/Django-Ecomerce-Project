# Generated by Django 4.1.1 on 2023-02-16 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0007_customer_delete_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
