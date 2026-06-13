from django.shortcuts import render
from .models import Zajezdy  # Ujisti se, že importuješ svůj správný model zájezdů
from django.shortcuts import get_object_or_404

# Tvoje stávající funkce pro hlavní stranu
def index(request):
    top_nabidky = Zajezdy.objects.all().order_by('cena')[:6]
    return render(request, 'traveling_app/index.html', {'zajezdy_top': top_nabidky})

# --- SEM PŘIDEJ TUTO CHYBĚJÍCÍ FUNKCI ---
def seznam_zajezdu(request):
    # Načteme filtry z formuláře v index.html
    destinace = request.GET.get('destinace', '')
    doprava = request.GET.get('doprava', '')

    # Základní queryset všech zájezdů
    vysledky = Zajezdy.objects.all()

    # Filtrování podle toho, co zákazník zadal
    if destinace:
        vysledky = vysledky.filter(destination__nazev__icontains=destinace) # Případně jen destination__icontains podle tvého modelu
    if doprava:
        vysledky = vysledky.filter(doprava=doprava)

    return render(request, 'traveling_app/vsechny_zajezdy.html', {
        'zajezdy_vysledek': vysledky,
        'destinace': destinace,
        'doprava': doprava
    })
def detail_zajezdu(request, trip_id):

    zajezd = get_object_or_404(
        Zajezdy,
        trip_id=trip_id
    )

    return render(
        request,
        'traveling_app/detail_zajezdu.html',
        {'zajezd': zajezd}
    )