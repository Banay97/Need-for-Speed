# Generated by Django 5.1 on 2024-08-20 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need_for_speed_app', '0003_order_order_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
