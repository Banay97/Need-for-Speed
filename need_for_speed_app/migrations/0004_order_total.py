# Generated by Django 5.1 on 2024-08-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need_for_speed_app', '0003_alter_company_number_of_workers'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Total',
            field=models.IntegerField(default=0),
        ),
    ]
