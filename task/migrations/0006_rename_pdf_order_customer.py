# Generated by Django 3.2.4 on 2021-06-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20210611_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='pdf',
            new_name='customer',
        ),
    ]
