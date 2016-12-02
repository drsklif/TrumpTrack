from django import forms
from django.contrib import admin
from api.models.packaging_type import PackagingType
from api.models.vehicle_type import VehicleType
from api.models.tr_status import TransportationRequestStatus
from api.models.tr_type import TransportationRequestType
from api.models.driver import Driver
from api.models.cargo_state import CargoState
from api.models.cargo import Cargo
from api.models.add_service import AdditionalService
from api.models.parcel_size import ParcelSize

admin.site.register(PackagingType)
admin.site.register(VehicleType)
admin.site.register(TransportationRequestStatus)
admin.site.register(TransportationRequestType)
admin.site.register(Driver)
admin.site.register(CargoState)
admin.site.register(AdditionalService)


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        # widgets = {
        #     'size': forms.Select(),
        # }
        fields = "__all__"
    size=forms.ChoiceField(choices=(("-","---------"),) + ParcelSize.all, widget=forms.Select)


class CargoAdmin(admin.ModelAdmin):
    form = CargoForm

admin.site.register(Cargo, CargoAdmin)
