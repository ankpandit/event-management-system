# Generated by Django 4.1.13 on 2024-04-19 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_services_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='image',
            field=models.ImageField(default='nopic', upload_to='static'),
            preserve_default=False,
        ),
    ]