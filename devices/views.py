#views.py

from django.shortcuts import render, redirect
from .models import Device 
from netmiko import ConnectHandler  
import os

commands = [] # lista de comandos objetivo

def index(request):
    return render(request, 'index.html')

def verify(request):
    if request.method == 'POST':
        ip_list = request.FILES['ip_list'] 
        username = request.POST['username']
        password = request.POST['password']
        
        # Lógica para conectarse y verificar
        
        for ip in ip_list:
           device = Device()
           device.ip = ip 
           
           # Guardar resultados en modelo Device
           
           device.save()
           
        return redirect('results')

    return render(request, 'verify.html')

def results(request):

  devices = Device.objects.all()

  context = {
    'devices': devices 
  }

  return render(request, 'results.html', context)