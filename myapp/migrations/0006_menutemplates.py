# Generated by Django 4.2.1 on 2023-05-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_logger_date_remove_logger_files_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuTemplates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]