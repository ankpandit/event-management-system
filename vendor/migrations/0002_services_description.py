# Generated by Django 4.1.13 on 2024-04-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='description',
            field=models.CharField(default='best decorations', max_length=50),
            preserve_default=False,
        ),
    ]
