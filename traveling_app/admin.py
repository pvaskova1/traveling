from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Destinace, Zajezdy, Zakaznici, Rezervace

@admin.register(Destinace)
class DestinaceAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'zeme')
    search_fields = ('nazev', 'zeme')

@admin.register(Zajezdy)
class ZajezdyAdmin(admin.ModelAdmin):
    list_display = ('title', 'destination', 'zacatek', 'konec', 'cena', 'obsazeno', 'kapacita','typ_dovolene')
    list_filter = ('destination', 'zacatek', 'doprava',)
    search_fields = ('title',)

@admin.register(Zakaznici)
class ZakazniciAdmin(admin.ModelAdmin):
    list_display = ('prijmeni', 'jmeno', 'email', 'telefon', 'mesto')
    search_fields = ('prijmeni', 'email', 'telefon')

@admin.register(Rezervace)
class RezervaceAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'customer', 'trip', 'booking_date', 'stav', 'platba')
    list_filter = ('stav', 'platba', 'booking_date')
    # Umožní vyhledávat v rezervacích podle jména zákazníka nebo názvu zájezdu
    search_fields = ('customer__prijmeni', 'trip__title')