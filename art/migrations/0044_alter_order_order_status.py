# Generated by Django 4.1.1 on 2023-03-17 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0043_alter_order_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way'), ('Order Completed', 'Order Completed'), ('Order Cancled', 'Order Cancled')], default='Order Received', max_length=50),
        ),
    ]
