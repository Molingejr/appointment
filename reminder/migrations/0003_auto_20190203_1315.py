# Generated by Django 2.1.5 on 2019-02-03 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20190203_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 3, 13, 15, 6, 161175, tzinfo=utc)),
        ),
    ]
