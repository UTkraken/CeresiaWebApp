# Generated by Django 3.2.9 on 2021-11-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ceresia', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hike',
            name='duration',
        ),
    ]
