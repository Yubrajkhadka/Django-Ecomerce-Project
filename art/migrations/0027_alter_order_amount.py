# Generated by Django 4.1.1 on 2023-02-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0026_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
