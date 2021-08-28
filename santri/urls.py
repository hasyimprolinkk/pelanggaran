from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('santri/', views.santri, name='santri'),
    path('inputsantri/', views.inputsantri, name='inputsantri'),
    path('updatesantri/<str:pk>', views.updateSantri, name='updatesantri'),
    path('deletesantri/<str:pk>', views.deleteSantri , name='deletesantri'),
    path('walisantri/', views.waliSantri, name='walisantri'),
    path('inputwalisantri/', views.inputWaliSantri, name='inputwalisantri'),
    path('updatewalisantri/<str:pk>', views.updateWaliSantri, name='updatewalisantri'),
    path('deletewalisantri/<str:pk>', views.deleteWaliSantri, name='deletewalisantri'),
    path('pelanggaran/', views.pelanggaran, name='pelanggaran'),
    path('inputpelanggaran/', views.inputpelanggaran, name='inputpelanggaran'),
    path('updatepelanggaran/<str:pk>', views.updatePelanggaran, name='updatepelanggaran'),
    path('deletepelanggaran/<str:pk>', views.deletePelanggaran, name='deletepelanggaran'),
    path('pengurus/', views.pengurus, name='pengurus'),
    path('inputpengurus', views.inputpengurus, name='inputpengurus'),
    path('deletepengurus/<str:pk>', views.deletePengurus, name='deletepengurus'),
    path('export/xls/', views.export_xls, name='export_xls'),
    path('pelanggaranuser/', views.pelanggaranuser, name='pelanggaranuser'),
    path('inputpelanggaranuser/', views.inputpelanggaranuser, name='inputpelanggaranuser'),
    path('deletepelanggaranuser/<str:pk>', views.deletePelanggaranuser, name='deletepelanggaranuser'),
    path('laporan/', views.laporan, name='laporan'),
    path('getfoto/', views.getfoto, name='getfoto'),
    # path('autocomplete/', views.autocomplete, name='autocomplete')

    # path('profil/<no_induk>', views.profil, name='profil'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)