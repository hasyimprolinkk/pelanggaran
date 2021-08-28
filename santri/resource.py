from import_export import resources
from .models import Pelanggaran
from import_export.fields import Field

class PelanggaranResource(resources.ModelResource):
    nama_santri__nama = Field(attribute='nama_santri', column_name='Nama Santri')
    class Meta:
        model = Pelanggaran
        fields = ['nama_santri__nama', 'nama_pelanggaran', 'kategory', 'kejadian', 'keterangan']

