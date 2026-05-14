from django.shortcuts import render
from .models import Zajezdy

# Přehled všech zájezdů (hlavní stránka)

from .models import Zajezdy

def index(request):
    # Vezmeme 6 zájezdů z tvé tabulky (viz obrázek image_2bc4de.png)
    top_nabidky = Zajezdy.objects.all().order_by('cena')[:6]
    
    return render(request, 'traveling_app/index.html', {
        'zajezdy_top': top_nabidky
    })