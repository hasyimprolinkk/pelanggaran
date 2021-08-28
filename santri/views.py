import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.http import HttpResponse
from .filters import WaliSantriFilter, SantriFilter, PelanggaranFilter
from .resource import PelanggaranResource
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorators import tolakhalaman_ini, ijinkan_pengguna, pilihan_login
# Create your views here.

# def autocomplete(request):
#     if 'term' in request.GET:
#         qs = Santri.objects.filter(title__icontains=request.GET.get('term'))
#         title = list()
#         for santri in qs:
#             titles.append(santri.title)
#         return JsonResponse(titles, safe=False)
#     return render(request, 'templates/base.html')

def getfoto(request):
    santri = Santri.objects.get(id=request.GET.get('pk'))
    foto = santri.foto.name
    return HttpResponse(foto)

def telegram_bot(chat_id, message):
    # https://api.telegram.org/bot1837414090:AAEd-MMi0Z_NYxkHdNsQTbMNyhndwQCJycY/getUpdates
    bot_token = '1837414090:AAH5AB4hR_oX1xbDMsPs7F5N0RsimoLkFCY'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=HTML&text=' + message
    response = requests.get(send_text)
    return response.json()

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def export_xls(request):
    pln = PelanggaranResource()
    dataset = pln.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=pelangaran.xls'
    return response

@login_required(login_url='login')
@ijinkan_pengguna(yang_diizinkan=['admin']) 
@pilihan_login
def beranda(request):
    list_pelanggaran = Pelanggaran.objects.all()
    ringan = list_pelanggaran.filter(kategory='Ringan').count()
    sedang = list_pelanggaran.filter(kategory='Sedang').count()
    berat = list_pelanggaran.filter(kategory='Berat').count()
    total = list_pelanggaran.count()
    context = {
        'menu' : 'beranda',
        'page' : 'Selamat datang di beranda',
        'plnringan' : ringan,
        'plnsedang' : sedang,
        'plnberat' : berat,
        'totalpln' : total

    }
    return render(request, 'data/beranda.html', context)

def registerPage(request):
    context = {
        'menu': 'register',
        'page': 'Halaman Register',
	
    }
    return render(request, 'data/register.html', context)

@tolakhalaman_ini
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cocokan = authenticate(request, username=username, password=password)
        if cocokan is not None:
            login(request, cocokan)
            return redirect('beranda')
        else:
            messages.error(request, f"username/password salah")
            return redirect('login')
        
    context = {
        'menu': 'login',
        'page': 'Halaman Login',
        
    }
    return render(request, 'data/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def waliSantri(request):
    dataWali = WaliSantri.objects.order_by('-id')
    filterwali = WaliSantriFilter(request.GET, queryset=dataWali)
    dataWali = filterwali.qs
    context = {
        'menu' : 'Form Wali santri',
        'page' : 'Halaman Wali Santri',
        'formdatawali' : dataWali,
        'filter_wali_santri' : filterwali
    }
    return render(request, 'data/formwalisantri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def inputWaliSantri(request):
    formwalisantri = WaliSantriForm()
    if request.method =='POST':
        formsimpan = WaliSantriForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('walisantri')
    context = {
        'menu' : 'input wali santri',
        'page' : 'Halaman Input Wali Santri',
        'formwali': formwalisantri
    }
    return render(request,'data/inputwalisantri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def updateWaliSantri(request, pk):
	walisantriupdate = WaliSantri.objects.get(id=pk)
	formwalisantri = WaliSantriForm(instance=walisantriupdate)
	if request.method == 'POST':
		formupdate = WaliSantriForm(request.POST, instance=walisantriupdate)
		if formupdate.is_valid:
			formupdate.save()
			return redirect('walisantri')
	context = {
		'menu': 'Edit wali santri',
        'page': 'Halaman update wali santri',
		'formwali': formwalisantri
	}
	return render(request, 'data/inputwalisantri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def deleteWaliSantri(request, pk):
    walisantrihapus = WaliSantri.objects.get(id=pk)
    if request.method == 'POST':
        walisantrihapus.delete()
        return redirect ('walisantri')
    context = {
        'menu':'menu delete wali santri',
        'page':'halaman delete wali santri',
        'formhapuswalisantri': walisantrihapus
    }
    return render(request, 'data/delete_wali_santri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def santri(request):
    dataSantri = Santri.objects.order_by('-id')
    filtersantri = SantriFilter(request.GET, queryset=dataSantri)
    dataSantri = filtersantri.qs
    context = {
        'menu' : 'Form Santri',
        'page' : 'Halaman Santri',
        'formdata' : dataSantri,
        'filter_santri' : filtersantri
    }
    return render(request, 'data/formsantri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def inputsantri(request):
    formSantri = SantriForm()
    if request.method =='POST':
        formsimpan = SantriForm(request.POST, request.FILES)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('santri')
    context = {
        'menu' : 'input santri',
        'page' : 'Halaman Input Santri',
        'form': formSantri
    }
    return render(request,'data/inputsantri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def updateSantri(request, pk):
	santriupdate = Santri.objects.get(id=pk)
	formsantri = SantriForm(instance=santriupdate)
	if request.method == 'POST':
		formedit = SantriForm(request.POST, request.FILES, instance=santriupdate)
		if formedit.is_valid:
			formedit.save()
			return redirect('santri')
	context = {
		'menu': 'Edit santri',
        'page': 'Halaman update santri',
		'form': formsantri
	}
	return render(request, 'data/inputsantri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def deleteSantri(request, pk):
    santrihapus = Santri.objects.get(id=pk)
    if request.method == 'POST':
        santrihapus.delete()
        return redirect ('santri')
    context = {
        'menu':'menu delete santri',
        'page':'halaman delete santri',
        'formhapussantri': santrihapus
    }
    return render(request, 'data/delete_santri.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def pelanggaran(request):
    namaPelanggaran = Pelanggaran.objects.order_by('-id')
    context = {
        'menu' : 'pelanggaran',
        'page' : 'Halaman pelanggaran',
        'formpelanggaran' : namaPelanggaran,
    }
    return render(request, 'data/pelanggaran.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def inputpelanggaran(request):
    formpelanggaran = PelanggaranForm()
    if request.method =='POST':
        formsimpan = PelanggaranForm(request.POST)
        if formsimpan.is_valid:
            santri = formsimpan['nama_santri'].value()
            pelanggaran = formsimpan['nama_pelanggaran'].value()
            hukuman = formsimpan['hukuman'].value()
            datasantri = Santri.objects.get(id=santri)
            chat_id = datasantri.nama_wali.chat_id

            pesan = f'INFORMASI PELANGGARAN!\nkepada bapak/ibu {datasantri.nama_wali}. ananda {datasantri.nama} teridentifikasi melakukan pelanggaran {pelanggaran} dengan hukuman {hukuman}'
            formsimpan.save()

            msg = 'Berhasil menambahkan data pelanggaran!'
            if chat_id is not None :
                telegram_bot(chat_id, pesan)
                msg += ' dan mengirimkan detail kepada telegram wali santri.'

            messages.success(request, f'{msg}')
            return redirect('pelanggaran')
    context = {
        'menu' : 'input santri',
        'page' : 'Halaman Input Santri',
        'formpln': formpelanggaran
    }
    return render(request,'data/inputpelanggaran.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def updatePelanggaran(request, pk):
	pelanggaranupdate = Pelanggaran.objects.get(id=pk)
	formpelanggaran = PelanggaranForm(instance=pelanggaranupdate)
	if request.method == 'POST':
		formedit = PelanggaranForm(request.POST, instance=pelanggaranupdate)
		if formedit.is_valid:
			formedit.save()
			return redirect('pelanggaran')
	context = {
		'menu': 'Edit pelanggaran',
        'page': 'Halaman update pelanggaran',
		'formpln': formpelanggaran
	}
	return render(request, 'data/inputpelanggaran.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def deletePelanggaran(request, pk):
    pelanggaranhapus = Pelanggaran.objects.get(id=pk)
    if request.method == 'POST':
        pelanggaranhapus.delete()
        messages.success(request, f'Data pelanggaran berhasil dihapus!')
        return redirect ('pelanggaran')
    context = {
        'menu':'menu delete pelanggaran',
        'page':'halaman delete pelanggaran',
        'formhapuspelanggaran': pelanggaranhapus
    }
    return render(request, 'data/delete_pelanggaran.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def pengurus(request):
    data = Pengurus.objects.order_by('-id')
    context ={
        "menu" : 'Pengurus',
        "page" : 'Halaman Pengurus',
        'pengurus' : data
    }
    return render(request, 'data/pengurus.html', context)

@ijinkan_pengguna(yang_diizinkan=['admin']) 
@login_required(login_url='login')
def inputpengurus(request):
    form = PengurusForm()
    formpengurus = PengurusForm(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        if User.objects.filter(username = username).first():
            messages.success(request, 'Username sudah ada.')
            return redirect('inputpengurus')

        if password1 != password2:
            messages.success(request, 'Password Tidak sama')
            return redirect('inputpengurus')
        # user
        user = User.objects.create_user(username=username)
        user.set_password(password1)
        user.is_active = True
        user.save()
        # user

        # Group
        akses_pengurus = Group.objects.get(name='pengurus')
        user.groups.add(akses_pengurus)
        # Group

        # Karyawan
        formsimpanpengurus = formpengurus.save()
        formsimpanpengurus.user = user
        formsimpanpengurus.save()
        # Karyawan
        
        return redirect('pengurus')

    context ={
        "menu" : 'Input pengurus',
        "page" : 'Halaman Pengurus',
        "form" : form
        
    }
    return render(request, 'data/inputpengurus.html', context)

def deletePengurus(request, pk):
    deletepengurus = Pengurus.objects.get(id=pk)
    if request.method == 'POST':
        deletepengurus.delete()
        return redirect ('pengurus')
    context = {
        'menu':'menu delete pengurus',
        'page':'halaman delete pengurus',
        'formhapuspengurus': deletepengurus
    }
    return render(request, 'data/delete_pengurus.html', context)
# def profil(request, id_santri):
#     dataprofil = Santri.objects.get(id_santri = id_santri)

#     context = {
#         'menu' : 'profil', 
#         'page' : 'Halaman profil', 
#         'dataprofilsantri' : dataprofil
        
#     }
#     return render(request, 'data/account_setting.html', context)

# def profil(request, no_induk):
#     context ={}
  
#     # add the dictionary during initialization
#     context["data"] = Santri.objects.get(no_induk = no_induk)
          
#     return render(request, "data/profil_santri.html", context)

@ijinkan_pengguna(yang_diizinkan=['pengurus']) 
@login_required(login_url='login')
def pelanggaranuser(request):
    namaPelanggaran = Pelanggaran.objects.order_by('-id')
    context = {
        'menu' : 'pelanggaran',
        'page' : 'Halaman pelanggaran',
        'formpelanggaran' : namaPelanggaran
    }
    return render(request, 'userpage/pelanggaranuser.html', context)

@ijinkan_pengguna(yang_diizinkan=['pengurus']) 
@login_required(login_url='login')
def inputpelanggaranuser(request):
    formpelanggaran = PelanggaranForm()
    if request.method =='POST':
        formsimpan = PelanggaranForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('pelanggaran')
    context = {
        'menu' : 'input santri',
        'page' : 'Halaman Input Santri',
        'formpln': formpelanggaran
    }
    return render(request,'userpage/inputpelanggaranuser.html', context)

def deletePelanggaranuser(request, pk):
    pelanggaranhapus = Pelanggaran.objects.get(id=pk)
    if request.method == 'POST':
        pelanggaranhapus.delete()
        return redirect ('pelanggaranuser')
    context = {
        'menu':'menu delete pelanggaran',
        'page':'halaman delete pelanggaran',
        'formhapuspelanggaran': pelanggaranhapus
    }
    return render(request, 'userpage/delete_pelanggaran_user.html', context)

def laporan(request):
    pelanggaran = Pelanggaran.objects.all()
    filterpelanggaran = PelanggaranFilter(request.GET, queryset=pelanggaran)
    filter_pel = filterpelanggaran.qs
    context = {
        'menu' : 'laporan',
        'filter_pln' : filterpelanggaran,
        'pelanggaran' : filter_pel,
    }
    return render(request, 'data/formlaporan.html', context)
