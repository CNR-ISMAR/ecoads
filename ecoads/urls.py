from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from ecos.views import EcosSiteList
from ecos.views import EcosSiteDetailView, sitesjson

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
import ecos.dashplotly

urlpatterns = [

    url('^example$', TemplateView.as_view(template_name='plotly/plotly.html'), name="example"),

    path('django_plotly_dash/', include('django_plotly_dash.urls')),

    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),

    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'', include('allauth.urls')), #tolto account di mezzo 
    
    url(r'sitesjson/$', sitesjson),
    
    url(r'sites/$', EcosSiteList.as_view()),

    url(r'sites/(?P<sitetype>[\w]+)/$', EcosSiteList.as_view()),

    path('site/<slug:slug>/', EcosSiteDetailView.as_view(), name='site-view'),

    

]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:

    url(r"", include(wagtail_urls)),

    
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
