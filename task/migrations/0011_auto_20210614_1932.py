# Generated by Django 3.2.4 on 2021-06-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20210614_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='collected_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='otp',
            field=models.IntegerField(default=-1),
        ),
    ]