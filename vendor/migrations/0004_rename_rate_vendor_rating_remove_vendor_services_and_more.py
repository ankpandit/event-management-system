# Generated by Django 4.1.13 on 2024-04-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_services_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='rate',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='services',
        ),
        migrations.AddField(
            model_name='vendor',
            name='customerType',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vendor',
            name='description',
            field=models.CharField(default='asd', max_length=50),
            preserve_default=False,
        ),
    ]
