from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def preowned_cars(request):
    return render(request, 'home/preowned_cars.html')

def other_services(request):
    return render(request, 'home/other_services.html')
