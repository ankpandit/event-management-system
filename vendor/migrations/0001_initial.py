# Generated by Django 4.1.13 on 2024-04-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorname', models.CharField(max_length=50)),
                ('serviceName', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendorname', models.CharField(max_length=50)),
                ('rate', models.IntegerField()),
                ('services', models.CharField(max_length=500)),
            ],
        ),
    ]
