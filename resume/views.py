from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import Resim  # Yeni modelimizi dahil ettik
# Create your views here.
def home(request):
    return render(request,'home.html')
def about (request):
    return render (request,"about.html")
def contact(request):
    return render (request,"contact.html")

def painting(request):
    eserler = Resim.objects.all()  # Veritabanındaki tüm resimleri alıyoruz
    return render(request, "painting.html", {"eserler": eserler})







