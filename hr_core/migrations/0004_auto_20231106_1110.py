# Generated by Django 2.2.2 on 2023-11-06 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_core', '0003_auto_20231104_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='user_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
