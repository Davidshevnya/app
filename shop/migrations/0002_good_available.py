# Generated by Django 4.2.10 on 2024-02-17 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]