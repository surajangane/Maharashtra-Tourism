# Generated by Django 4.1.2 on 2022-11-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('where', models.CharField(max_length=50)),
                ('guest', models.IntegerField()),
                ('arrivals', models.DateField()),
                ('leaving', models.DateField()),
            ],
        ),
    ]
