# Generated by Django 4.2.1 on 2023-05-19 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_logger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logger',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='logger',
            name='files',
        ),
        migrations.AddField(
            model_name='logger',
            name='time_Log',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Enter exact Time!'),
            preserve_default=False,
        ),
    ]
