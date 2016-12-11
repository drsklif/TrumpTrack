import django_filters
from api.models.contractor import Contractor


class ContractorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name="name", lookup_expr="contains")

    class Meta:
        model = Contractor
        fields = ['name']
