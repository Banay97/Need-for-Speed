# Generated by Django 5.1 on 2024-08-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('need_for_speed_app', '0008_order_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='link',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='context',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='status',
        ),
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
