# Generated by Django 2.1.7 on 2019-03-06 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='time',
            field=models.TextField(max_length=255),
        ),
    ]
