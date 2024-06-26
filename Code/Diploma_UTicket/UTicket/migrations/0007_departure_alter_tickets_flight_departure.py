# Generated by Django 5.0.1 on 2024-05-17 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTicket', '0006_city_alter_tickets_city_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='tickets',
            name='flight_departure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UTicket.departure'),
        ),
    ]
