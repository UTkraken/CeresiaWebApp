# Import
import pandas as pd
import numpy as np
from numpy.random import randint
# Model
from .models import Hike, User, SerialNumber, Species


def clear_database():
    Hike.objects.all().delete()
    User.objects.all().delete()
    SerialNumber.objects.all().delete()
    Species.objects.all().delete()


def generate_serial_number():
    for i in range(2500):
        s = SerialNumber()
        s.serial_number = str(i + 1)
        s.save()


def clean_and_add_hikes_data():
    df = pd.read_csv('dataset/short_hikes.csv')
    for i in df.iterrows():
        h = Hike()
        try:
            h.name = str(i[1]["name"])
            h.location = str(i[1]["the_geom"])
            h.county = str(randint(1, 95))
            h.duration = str(i[1]["duration"])
            h.distance = str(i[1]["distance"])
            h.save()
        except:
            continue


def import_test_user():
    u = User()
    u.lastname = 'Gimard'
    u.firstname = 'Yvan'
    u.email = 'yvan.gimard@ceresia.com'
    u.password = 'lebddcestgenial73'
    u.serial_number = SerialNumber.objects.get(serial_number=73)
    u.save()

    u = User()
    u.lastname = 'Burgard'
    u.firstname = 'Thomas'
    u.email = 'thomas.burgard@ceresia.com'
    u.password = 'lebddcestgenial74'
    u.serial_number = SerialNumber.objects.get(serial_number=74)
    u.save()


def import_some_species():
    data = pd.read_csv('dataset/short_species.csv')
    for i in data.iterrows():
        try:
            s = Species()
            s.family = str(i[1]["SPGROUP"])
            s.scientific_name = str(i[1]["SPECIESNAME"])
            s.weight = str(randint(3, 250))
            s.height = str(randint(3, 200))
            s.save()
        except:
            continue


def generate_data_docker():
    clear_database()
    generate_serial_number()
    clean_and_add_hikes_data()
    import_some_species()
    import_test_user()
    print("All data is addeed !")
