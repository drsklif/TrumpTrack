from api.models.property_type import PropertyType
from api.models.contractor_status import ContractorStatus
from api.models.contractor import Contractor
from api.models.parcel_size import ParcelSize
from api.models.tr_type import TransportationRequestType
from api.models.tr_status import TransportationRequestStatus
from api.models.tr import TransportationRequest
from rest_framework import serializers


class PropertyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PropertyType
        fields = ('url', 'name',)


class ContractorStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContractorStatus
        fields = ('url', 'name', )


class ContractorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contractor
        fields = ('url', 'name', 'full_name', 'property_type', 'status', 'phone', 'fax', 'email', 'address_legal',
                  'address_actual', 'address_mailing', 'notes',)


class ParcelSizeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ParcelSize
        fields = ('url', 'size', )


class TransportationRequestTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransportationRequestType
        fields = ('url', 'name',)


class TransportationRequestStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransportationRequestStatus
        fields = ('url', 'name', )


class TransportationRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransportationRequest
        fields = ('url', 'client', 'address_from', 'address_to', 'date_departure', 'description', 'weight', 'size',
                  'type', 'status',)
