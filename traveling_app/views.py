from django.shortcuts import render, get_object_or_404
from .models import Zajezdy

def index(request):
    # Načte 6 zájezdů pro úvodní stranu
    top_zajezdy = Zajezdy.objects.all().order_by('cena')[:6]
    return render(request, 'traveling_app/index.html', {'zajezdy': top_zajezdy})

def seznam_zajezdu(request):
    destinace = request.GET.get('destinace', '')
    doprava = request.GET.get('doprava', '')
    
    vysledky = Zajezdy.objects.all()
    
    if destinace:
        vysledky = vysledky.filter(destination__nazev__icontains=destinace)
    if doprava and doprava != 'Nerozhoduje':
        vysledky = vysledky.filter(doprava=doprava)
        
    return render(request, 'traveling_app/vsechny_zajezdy.html', {
        'zajezdy': vysledky,
        'destinace': destinace,
        'doprava': doprava
    })

def detail(request, zajezd_id):
    zajezd = get_object_or_404(Zajezdy, trip_id=zajezd_id)
    return render(request, 'traveling_app/detail.html', {'zajezd': zajezd})