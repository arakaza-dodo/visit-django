# Generated by Django 4.2.6 on 2023-10-17 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Visit', '0012_transport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transport',
            name='address',
        ),
    ]
