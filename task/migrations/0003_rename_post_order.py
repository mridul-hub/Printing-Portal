# Generated by Django 3.2.4 on 2021-06-11 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20210611_0623'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Order',
        ),
    ]
