# Generated by Django 4.1.1 on 2023-03-24 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0049_remove_product_average_rating_delete_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
    ]
