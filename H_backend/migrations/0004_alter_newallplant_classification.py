# Generated by Django 4.2.11 on 2024-08-01 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('H_backend', '0003_newallplant_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newallplant',
            name='classification',
            field=models.CharField(max_length=255),
        ),
    ]
