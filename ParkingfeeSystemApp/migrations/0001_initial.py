# Generated by Django 3.0 on 2019-12-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile_number', models.IntegerField(max_length=10)),
                ('entry', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]