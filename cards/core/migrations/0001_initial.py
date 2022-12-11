# Generated by Django 4.1.4 on 2022-12-09 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvc', models.IntegerField()),
                ('number_cart', models.CharField(max_length=19)),
                ('date_start', models.DateTimeField(auto_now_add=True)),
                ('date_stop', models.DateTimeField(default=datetime.datetime(2023, 12, 9, 19, 9, 45, 252334, tzinfo=datetime.timezone.utc))),
                ('date_use', models.DateTimeField(auto_now=True)),
                ('amount_cash', models.IntegerField()),
                ('status', models.CharField(choices=[('WORK', 'WORKING'), ('STOP', 'STOPPED'), ('NOT ACTIVATED', 'NOT_ACTIVATED')], default='WORK', max_length=14)),
            ],
        ),
    ]
