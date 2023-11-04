# Generated by Django 2.2.2 on 2023-11-02 15:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_id', models.CharField(max_length=255)),
                ('employee_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('job_role', models.CharField(choices=[('MANAGER', 'MANAGER'), ('JUNIOR_ENGINEER', 'JUNIOR_ENGINEER'), ('SENIOR_ENGINEER', 'SENIOR_ENGINEER')], max_length=30)),
                ('department', models.CharField(choices=[('HR', 'HR'), ('ENGINEERING', 'ENGINEERING')], max_length=255)),
                ('joining_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in_datetime', models.DateTimeField()),
                ('clock_out_datetime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'), ('HOLIDAY', 'HOLIDAY')], max_length=15)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='hr_core.Employee')),
            ],
        ),
    ]