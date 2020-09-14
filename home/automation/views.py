from django.shortcuts import render
# from django.http import HttpResponse
import psutil


# Create your views here.

def index(request):
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().available
    memory = round(mem / 1024/ 1024)
    send = {"cpu": cpu, "memory": memory}
    return render(request, 'automation/index.html', send)
