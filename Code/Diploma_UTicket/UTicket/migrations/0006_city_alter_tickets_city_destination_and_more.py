# Generated by Django 5.0.1 on 2024-05-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UTicket', '0005_alter_tickets_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tickets',
            name='city_destination',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='city_of_departure',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='date_of_birth',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='first_name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='flight_departure',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='phone_number',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='plane_class',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='plane_place',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='second_name',
            field=models.TextField(max_length=100),
        ),
    ]
