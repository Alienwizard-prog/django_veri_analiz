from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.
def anasayfaView(requests):
    return HttpResponse("Merhaba django bu benim ilk uygulama 06.04.2025")