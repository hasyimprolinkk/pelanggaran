from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WaliSantri(models.Model):
    nama_wali = models.CharField(max_length=200, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    no_telpon = models.CharField(max_length=200, blank=True, null=True)
    chat_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        # return "%s" %(self.nama_wali)
        return self.nama_wali

    class Meta:
        verbose_name_plural ="Wali Santri" 

class Santri(models.Model):
    PENDIDIKAN=(
        ('UNIVERSITAS ZAINUL HASAN', 'UNIVERSITAS ZAINUL HASAN'),
        ('SMA Zainul Hasan', 'SMA Zainul Hasan'),
        ('MA Zainul Hasan' , 'MA Zainul Hasan'),
        ('SMP Zainul Hasan' , 'SMP Zainul Hasan'),
        ('MTS Zainul Hasan' , 'MTS Zainul Hasan'),
    )
    no_induk = models.CharField(max_length=10, unique = True, null=False)
    nama = models.CharField(max_length=200, blank=False, null=False)
    tgl_lahir = models.DateField(auto_now=False, auto_now_add=False)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    pendidikan = models.CharField(max_length=150, blank=False, null=False, choices=PENDIDIKAN)
    foto =  models.ImageField(null=True, blank=True)
    nama_wali = models.ForeignKey(WaliSantri, blank=False, null=True, on_delete=models.SET_NULL)

    # def save(self, *args, **kwargs):
    #     super(Santri, self).save(*args, **kwargs)

        # img = Image.open(self.profile_pic.path)

        # if img.height > 100 or img.width > 100:
        #     output_size = (100, 100)
        #     img.thumbnail(output_size)
        #     img.save(self.profile_pic.path)

    def __str__(self):
        # return "%s" %(self.nama_santri)
        return self.nama

    class Meta:
        verbose_name_plural = "Santri"

class Pengurus(models.Model):
    Staff = (
        ('Kepala Pondok', 'Kepala Pondok'),
        ('Keamanan', 'Keamanan'),
        ('Pendidikan', 'Pendidikan'),
        ('Sekertaris', 'Sekertaris'),
    )
    user = models.OneToOneField(User, blank =True, null=True, on_delete = models.CASCADE)
    nama_pengurus = models.CharField(max_length=200, blank=True, null=False)
    staff = models.CharField(max_length=200, blank=True, null=False, choices = Staff)
    no_telpon = models.CharField(max_length=200, blank=True, null=False)


    def __str__(self):
        return self.nama_pengurus
    class Meta:
        verbose_name_plural = "Pengurus"

class Pelanggaran(models.Model):
    Category = (
        ('Ringan', 'Ringan'),
        ('Sedang', 'Sedang'),
        ('Berat', 'Berat'),
    )

    # Status = (
    #     ('Proses', 'Proses'),
    #     ('Selesai', 'Selesai'),
    # )
    nama_santri = models.ForeignKey(Santri, blank=True, null=True, on_delete=models.SET_NULL)
    nama_pelanggaran = models.CharField(max_length=200, blank=True, null=True)
    kategory = models.CharField(max_length=150, blank=True, null=False, choices=Category)
    kejadian = models.DateField(blank=False, null=False)
    keterangan = models.CharField(max_length=200, blank=True, null=False)
    hukuman = models.CharField(max_length=150, blank=True, null=False)

    def __str__(self):
        return "%s" %(self.nama_santri)
        # return self.nama_santri
    class Meta:
        verbose_name_plural = "Laporan Pelanggaran"
