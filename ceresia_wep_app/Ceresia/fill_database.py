# Import
import pandas as pd
from numpy.random import randint
# Model
from Ceresia.models import Hike, User, SerialNumber, Species


def generate_serial_number():
    for i in range(2500):
        s = SerialNumber()
        s.serial_number = str(i + 1)
        s.save()


def clean_and_add_hikes_data():
    df = pd.read_csv('dataset/france_hiking_foot_routes_line.csv')
    # Remove all hikes with a empty name
    df_clean = df.loc[df['name'].notnull()]
    for i in df_clean.iterrows():
        h = Hike()
        h.name = str(i[1]["name"])
        h.location = str(i[1]["the_geom"])
        h.county = str(randint(1, 95))
        h.duration = str(i[1]["distance"])
        h.save()

    return df_clean.head()


def import_test_user():
    u = User()
    u.lastname = 'Gimard'
    u.firstname = 'Yvan'
    u.email = 'yvan.gimard@ceresia.com'
    u.password = 'lebddcestgenial73'
    u.serial_number = SerialNumber.objects.get(pk=73)
    u.save()

    u.lastname = 'Burgard'
    u.firstname = 'Thomas'
    u.email = 'thomas.burgard@ceresia.com'
    u.password = 'lebddcestgenial74'
    u.serial_number = SerialNumber.objects.get(pk=74)
    u.save()


def import_some_species():
    data = pd.read_csv('dataset/Emerald_2020_SPECIES.csv')
    for i in data.iterrows():
        s = Species()
        s.family = str(i[1]["SPGROUP"])
        s.scientific_name = str(i[1]["SPECIESNAME"])
        s.weight = str(randint(3, 250))
        s.height = str(randint(3, 200))
        s.save()
