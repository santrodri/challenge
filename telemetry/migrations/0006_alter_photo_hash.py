# Generated by Django 5.2.3 on 2025-07-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemetry', '0005_remove_photo_description_photo_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='hash',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
