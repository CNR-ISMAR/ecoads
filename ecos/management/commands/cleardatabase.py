from django.core.management.base import BaseCommand, CommandError

import swagger_client                                                                                                                                                                    
from swagger_client.api_client import ApiClient
from ecos.models import EcosSite

class Command(BaseCommand):
    help = 'Import sites from deims sdr'


    def handle(self, *args, **options):

                                                                                                                                                                                                 
        api_client = ApiClient()
        api_client.configuration.host = "https://deims.org/api"
        api = swagger_client.DefaultApi(api_client=api_client)
        sites = api.sites_get()

        for s in EcosSite.objects.all():
            s.delete()

        