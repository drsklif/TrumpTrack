from django.conf.urls import url

from site_app.views import index, create_request, view_request

__author__ = 'ildyakov'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^create_request/', create_request, name='create_request'),
    url(r'^view_request/(?P<request_id>[0-9]+)/', view_request, name='view_request'),
]
