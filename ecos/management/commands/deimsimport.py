from django.core.management.base import BaseCommand, CommandError
import json
import swagger_client                                                                                                                                                                    
from swagger_client.api_client import ApiClient
from ecos.models import EcosSite, Parameter
from django.contrib.gis.geos import GEOSGeometry, LineString, Point, Polygon, MultiPolygon, MultiLineString

from urllib.request import urlopen
from bs4 import BeautifulSoup


class Command(BaseCommand):
    help = 'Import sites from deims sdr'

    def handle(self, *args, **options):

                                                                                                                                                                                                 
        api_client = ApiClient()
        api_client.configuration.host = "https://deims.org/api"
        api = swagger_client.DefaultApi(api_client=api_client)
        sites = api.sites_get()

        for s in sites:
            site = api.sites_resource_id_get(resource_id=s.id.suffix)
            if not (set(['Italy', 'Slovenia', 'Croatia']) & set(site.attributes.geographic.country)):
                continue
            print(site.id.prefix, site.id.suffix, site.title, site.attributes.geographic.country)

            domain_area = None
            if site.attributes.geographic.boundaries is not None:
                domain_area = GEOSGeometry(site.attributes.geographic.boundaries, srid=4326)

                if domain_area and (isinstance(domain_area, LineString) 
                                    or (domain_area, MultiLineString)):
                    domain_area = domain_area.buffer(0.0001)

                if domain_area and isinstance(domain_area, Polygon):
                    domain_area = MultiPolygon(domain_area)

            obj, created = EcosSite.objects.get_or_create(
                suffix = site.id.suffix,
                defaults= {'location' : GEOSGeometry(site.attributes.geographic.coordinates, srid=4326)}
                
            )
            
            obj.data = json.loads(api_client.last_response.data) 
            obj.denomination = site.title
            obj.description = site.attributes.general.abstract
            obj.domain_area = domain_area 
            obj.website= site.id.prefix+site.id.suffix
            obj.last_update = site.changed
            obj.img = imgimport(site.id.suffix)
            obj.location = GEOSGeometry(site.attributes.geographic.coordinates, srid=4326)

            obj.save()

            if site.attributes.focus_design_scale.parameters is not None:
                #print(site.attributes.focus_design_scale.parameters.__class__, site.attributes.focus_design_scale.parameters.__dict__)
                #print(site.attributes.focus_design_scale.parameters)
                #print(site.attributes.focus_design_scale.parameters[0].label)
                #print(site.attributes.focus_design_scale.parameters[0].uri)

                preferred_label_en = site.attributes.focus_design_scale.parameters[0].label
                
                obj, created = Parameter.objects.get_or_create(
                    uri = site.attributes.focus_design_scale.parameters[0].uri,
                    defaults={'preferred_label_en': preferred_label_en}
                )

                preferred_label_en = preferred_label_en
                
            #./manage.py shell< ecoads/sandbox.py

def imgimport(suffix):

    URL = "https://deims.org/{}".format(suffix)  #provare con alre pagine prima 
    soup = BeautifulSoup(urlopen(URL), "html5lib")
    img_div = soup.find('div', {"id": "bootstrap-panel--3"})
    if img_div is None or img_div.img is None:
        return None
    img = img_div.img['data-lazy'] #funziona ed ha una / davanti 

    return "https://deims.org{}".format(img)

