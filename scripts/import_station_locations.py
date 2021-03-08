from measurements.models import Location, Station, SourceType, Network
from django.contrib.gis.geos import Point
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd
import re

IOC = "http://www.ioc-sealevelmonitoring.org/station.php?code={}"

stations = (
        ('Trieste', 'TR22'),
        ('Venice', 'VE19'),
        ('Ancona', 'AN15'),
        ('S. Benedetto Del Tronto', 'SB36'),
        ('Stari Grad', 'stari'),
        ('Vela Luka', 'vela'),
        ('Sobra', 'sobr'),
        ('Otranto', 'OT15'),
        ('Kerkyra, Corfu', 'corf'),
        ('Crotone', 'CR08'),
        ('Le Castella', 'lcst'),
        ('Itea', 'itea'),
        ('Panormos', 'pano'),
        ('Aigio', 'aigi'),
        ('Katakolo', 'kata'),
        # ('Kyparissia', 'kypa'),
        )


ioc_source, created = SourceType.objects.get_or_create(code='ioc')
ioc_network, created = Network.objects.get_or_create(code='ioc')

# IOC stations
for label, code in stations:
    r = requests.get(IOC.format(code))
    # print(r.text)
    soup = BeautifulSoup(r.text)
    for elem in soup(text='Latitude   '):
        lat = float(elem.find_next('td').contents[0])
    for elem in soup(text='Longitude   '):
        lon = float(elem.find_next('td').contents[0])
    # print(lon, lat)
    l, created = Location.objects.get_or_create(label=label)
    l.geo = Point(lon, lat)
    l.save()
    # print(label, l)
    s, created = Station.objects.get_or_create(code=code,
                                               label=label,
                                               source=ioc_source,
                                               network=ioc_network,
                                               location=l)

