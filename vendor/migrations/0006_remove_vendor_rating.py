# Generated by Django 4.1.13 on 2024-04-19 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0005_vendor_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='rating',
        ),
    ]