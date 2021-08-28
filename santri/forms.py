from django import forms
from django.forms import ModelForm, DateTimeInput
from .models import *

class SantriForm(ModelForm):

    class Meta:
        model = Santri
        fields = ['nama_wali','no_induk','nama','tgl_lahir', 'alamat', 'pendidikan', 'foto']
        
        # YEARS= [x for x in range(1940,2021)]

        widgets = {
            'nama_wali': forms.Select(attrs={'class': 'form-select'}),
            'no_induk': forms.TextInput(attrs={'class': 'form-select'}),
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'tgl_lahir': forms.DateInput(format = '%m-%d-%Y',attrs={'type': 'date'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'pendidikan': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'nama_wali' : 'Orang tua',
            'no_induk': 'No induk',
            'nama': 'Nama Santri',
            'tgl_lahir': 'Tanggal lahir',
            'alamat' : 'Alamat',
            'pendidikan' : 'Lembaga',
        }

class WaliSantriForm(ModelForm):

    class Meta:
        model = WaliSantri
        fields = '__all__'

        widgets = {
            'nama_wali': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control'}),
            'no_telpon': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'nama_wali' : 'Nama Wali',
            'alamat' : 'Alamat',
            'no_telpon' : 'Nomer telepon',
        }

class PelanggaranForm(ModelForm):

    class Meta:
        model = Pelanggaran
        fields = ['nama_santri', 'nama_pelanggaran', 'kategory', 'kejadian', 'keterangan', 'hukuman']

        widgets = {
            'nama_santri' : forms.Select(attrs={'class': 'form-control'}),
            'nama_pelanggaran' : forms.TextInput(attrs={'class': 'form-control'}),
            'kategory' : forms.Select(attrs={'class': 'form-control'}),
            'kejadian' : forms.DateInput(format = '%m-%d-%Y',attrs={'type': 'date'}),
            'keterangan' : forms.Textarea(attrs={'class': 'form-control', 'type': 'textarea'}),
            'hukuman' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nama_santri' : 'Nama Santri',
            'nama_pelanggaran' : 'Pelanggaran',
            'kategory' : 'Kategori Pelanggaran',
            'kejadian' : 'Tanggal Kejadian',
            'keterangan' : 'Sebab Pelanggaran',
            'hukuman' : 'hukuman',
        }

class PengurusForm(ModelForm):

    class Meta:
        model = Pengurus
        fields = '__all__'
        exclude = ['user']
        labels = {
            'nama_pengurus' : 'Nama Pengurus',
            'staff' : 'Bagian',
            'no_telpon' : 'Nomer telepon',
        }