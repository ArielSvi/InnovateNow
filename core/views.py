from django.shortcuts import render
from .models import NavbarItem, AboutUs, Service

def home(request):
    navbar_items = NavbarItem.objects.all()
    return render(request, 'core/home.html', {'navbar_items': navbar_items})


def about_us(request):
    about_us_content = AboutUs.objects.first()
    navbar_items = NavbarItem.objects.all()
    return render(request, 'core/about_us.html', {'about_us_content': about_us_content, 'navbar_items': navbar_items})


def services(request):
    navbar_items = NavbarItem.objects.all()
    services = Service.objects.all()
    return render(request, 'core/services.html', {'navbar_items': navbar_items, 'services': services})