import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

class WaliSantriFilter(django_filters.FilterSet):
    nama_wali = CharFilter(field_name="nama_wali", lookup_expr='icontains')

    class Meta:
        model = WaliSantri
        fields = ['nama_wali']

class SantriFilter(django_filters.FilterSet):
    nama_santri = CharFilter(field_name="nama_santri", lookup_expr='icontains')

    class Meta:
        model = Santri
        fields = ['nama_santri']

class PelanggaranFilter(django_filters.FilterSet):
    tglmulai = DateFilter(field_name="kejadian", lookup_expr='gte')
    tglakhir = DateFilter(field_name="kejadian", lookup_expr='lte')

    class Meta:
        model = Pelanggaran
        fields ='__all__'