# Generated by Django 5.0.6 on 2024-06-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='horsepower',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
    ]
