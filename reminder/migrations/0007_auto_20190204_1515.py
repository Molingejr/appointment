# Generated by Django 2.1.5 on 2019-02-04 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0006_auto_20190204_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='tel',
            field=models.CharField(max_length=20),
        ),
    ]