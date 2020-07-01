from django.core.management.base import BaseCommand, CommandError

import swagger_client                                                                                                                                                                    
from swagger_client.api_client import ApiClient
from ecos.models import EcosSite
from django.contrib.gis.geos import GEOSGeometry, LineString, Point, Polygon, MultiPolygon, MultiLineString

class Command(BaseCommand):
    help = 'Import sites from deims sdr'

    def handle(self, *args, **options):

                                                                                                                                                                                                 
        api_client = ApiClient()
        api_client.configuration.host = "https://deims.org/api"
        api = swagger_client.DefaultApi(api_client=api_client)
        sites = api.sites_get()
      

        #suffix = ['4e645ab1-61d5-4414-92a2-eeb912f5e515']

        for s in sites:
            site = api.sites_resource_id_get(resource_id=s.id.suffix)
            if not (set(['Italy', 'Slovenia']) & set(site.attributes.geographic.country)):
                continue
            print(site.id.suffix, site.title, site.attributes.geographic.country)

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
                location = GEOSGeometry(site.attributes.geographic.coordinates, srid=4326)
            )

            obj.data = api_client.last_response.data
            obj.denomination =site.title 
            obj.description = site.attributes.general.abstract
            obj.domain_area = domain_area 
            #website= site.attributes.contact.site_url[0].value, #deims  + suffix 
            obj.last_update = site.changed 

            obj.save()
            
            #./manage.py shell< ecoads/sandbox.py

