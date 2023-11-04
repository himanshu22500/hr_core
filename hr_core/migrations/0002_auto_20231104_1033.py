# Generated by Django 2.2.2 on 2023-11-04 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='clock_in_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('HOLIDAY', 'HOLIDAY'), ('SINGLE_PUNCH_ABSENT', 'SINGLE_PUNCH_ABSENT')], max_length=15),
        ),
    ]