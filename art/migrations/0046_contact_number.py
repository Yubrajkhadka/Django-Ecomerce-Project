# Generated by Django 4.1.1 on 2023-03-19 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0045_alter_admin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default=False, max_length=10),
        ),
    ]
