# Generated by Django 2.2.2 on 2023-11-04 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_core', '0002_auto_20231104_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='clock_in_datetime',
            field=models.DateTimeField(),
        ),
    ]
