from django.conf.urls import url, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'propertytypes', views.PropertyTypeViewSet)
router.register(r'contractorstatuses', views.ContractorStatusViewSet)
router.register(r'contractors', views.ContractorViewSet)
router.register(r'parcelsizes', views.ParcelSizeViewSet)
router.register(r'transportationrequesttypes', views.TransportationRequestTypeViewSet)
router.register(r'transportationrequeststatuses', views.TransportationRequestStatusViewSet)
router.register(r'transportationrequests', views.TransportationRequestViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
