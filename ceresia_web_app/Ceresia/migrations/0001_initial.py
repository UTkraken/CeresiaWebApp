# Generated by Django 3.2.9 on 2021-11-22 08:28

from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', django_bleach.models.BleachField(max_length=150)),
                ('location', django_bleach.models.BleachField(max_length=150)),
                ('rating', django_bleach.models.BleachField(max_length=150, null=True)),
                ('county', django_bleach.models.BleachField(max_length=150)),
                ('duration', django_bleach.models.BleachField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SerialNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', django_bleach.models.BleachField()),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', django_bleach.models.BleachField(max_length=150)),
                ('scientific_name', django_bleach.models.BleachField(max_length=150)),
                ('weight', django_bleach.models.BleachField(max_length=150)),
                ('height', django_bleach.models.BleachField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', django_bleach.models.BleachField(max_length=50)),
                ('firstname', django_bleach.models.BleachField(max_length=50)),
                ('email', django_bleach.models.BleachField(max_length=100)),
                ('password', django_bleach.models.BleachField(max_length=50)),
                ('serial_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceresia.serialnumber')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceresia.user')),
                ('num_hike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceresia.hike')),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('path', django_bleach.models.BleachField()),
                ('scientific_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceresia.species')),
                ('serial_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ceresia.serialnumber')),
            ],
        ),
    ]
