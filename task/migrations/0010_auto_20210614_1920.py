# Generated by Django 3.2.4 on 2021-06-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0009_auto_20210612_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='customer_email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='customer_name',
        ),
        migrations.AlterField(
            model_name='order',
            name='cost',
            field=models.IntegerField(default=1),
        ),
    ]
