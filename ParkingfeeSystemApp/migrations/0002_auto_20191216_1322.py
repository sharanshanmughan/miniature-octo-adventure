# Generated by Django 3.0 on 2019-12-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParkingfeeSystemApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='mobile_number',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]
