# Generated by Django 4.1.4 on 2023-01-12 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='', regex='^\\+?3?8?0\\d{2}[- ]?(\\d[ -]?){7}$')])),
                ('e_mail', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(regex='[a-zA-Z0-9][a-zA-Z0-9_\\-]*(\\.[a-zA-Z0-9_\\-]+)?@([a-zA-Z0-9_]|\\-)+(\\.[a-zA-Z0-9_]{1,10})+')])),
                ('persons', models.PositiveSmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_time_order', models.DateTimeField(auto_now=True)),
                ('manager_date_processed', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]