# Generated by Django 4.1.1 on 2023-03-15 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0039_alter_order_order_status_alter_orderitem_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.ImageField(upload_to='photos/products'),
        ),
    ]
