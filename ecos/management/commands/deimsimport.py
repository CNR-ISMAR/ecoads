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
      

        #suffixies = ['4e645ab1-61d5-4414-92a2-eeb912f5e515',
        #'e8a54b19-642a-4dd3-b5a4-253c492a19de', 
        #'5c3d96e4-1db3-4615-a982-9eab819d613a', 
        #'ede67a31-079a-4db5-b3a2-83b22054c661',
        #]



        #import datetime
        #result = datetime.datetime.strptime('2017-01-12T14:12:06.000-0500','%Y-%m-%dT%H:%M:%S.%f%z')
        #print(result)

        for s in sites:
        #for s in suffixies:
            site = api.sites_resource_id_get(resource_id=s.id.suffix)
            #site = api.sites_resource_id_get(resource_id=s)
           #fatto con Slovenia and Italy 
            if not ('Italy' in site.attributes.geographic.country):
                continue
                #print(site.id.suffix, site.title, site.attributes.geographic.country)
                #print(obj)
            print(site.id.suffix, site.title, site.attributes.geographic.country)


            domain_area = None
            if site.attributes.geographic.boundaries is not None:
                #print(site.attributes.geographic.boundaries)
                domain_area = GEOSGeometry(site.attributes.geographic.boundaries, srid=4326)

                if domain_area and (isinstance(domain_area, LineString) 
                                    or (domain_area, MultiLineString)):
                    domain_area = domain_area.buffer(0.0001)

                if domain_area and isinstance(domain_area, Polygon):
                    domain_area = MultiPolygon(domain_area)
                
                 
                        



            obj, created = EcosSite.objects.get_or_create(
                suffix = site.id.suffix, 
                denomination=site.title, 
                description = site.attributes.general.abstract, 
                domain_area = domain_area, 
                location= GEOSGeometry(site.attributes.geographic.coordinates, srid=4326),
                #website= site.attributes.contact.site_url[0].value, #deims  + suffix 
                #last_update = site.changed,
            )
            

            
        
            
            #./manage.py shell< ecoads/sandbox.py



        #for poll_id in options['poll_ids']:
           # try:
            #    poll = Poll.objects.get(pk=poll_id)
            #except Poll.DoesNotExist:
                #raise CommandError('Poll "%s" does not exist' % poll_id)

            #poll.opened = False
            #poll.save()

           # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))


