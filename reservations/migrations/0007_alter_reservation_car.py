# Generated by Django 5.0.6 on 2024-06-15 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0006_alter_reservation_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reservations', to='reservations.car'),
        ),
    ]
