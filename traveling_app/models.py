from django.db import models

# Create your models here.
from django.db import models

class Destinace(models.Model):
    destination_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=80)
    zeme = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.nazev} ({self.zeme})"

    class Meta:
        verbose_name_plural = "Destinace"


class Zajezdy(models.Model):
    trip_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    zacatek = models.DateField()
    konec = models.DateField()
    cena = models.IntegerField()
    # Relace na Destinace
    destination = models.ForeignKey(Destinace, on_delete=models.CASCADE, db_column='destination_id')
    kapacita = models.IntegerField()
    obsazeno = models.IntegerField()
    doprava = models.CharField(max_length=30)
    typ_dovolene = models.CharField(max_length=50, default='Pobytový', verbose_name="Typ dovolené")
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Zájezdy"


class Zakaznici(models.Model):
    customer_id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=50)
    prijmeni = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    telefon = models.CharField(max_length=20)
    ulice = models.CharField(max_length=50)
    c_p = models.CharField(max_length=10, db_column='č.p.')
    mesto = models.CharField(max_length=40)
    psc = models.CharField(max_length=10)
    stat = models.CharField(max_length=50)

    title = models.CharField(max_length=100)

    obrazek = models.ImageField(
        upload_to='zajezdy/',
        blank=True,
        null=True
    )

    zacatek = models.DateField()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

    class Meta:
        verbose_name_plural = "Zákazníci"


class Rezervace(models.Model):
    booking_id = models.AutoField(primary_key=True)
    # Relace na Zakaznici a Zajezdy
    customer = models.ForeignKey(Zakaznici, on_delete=models.CASCADE, db_column='customer_id')
    trip = models.ForeignKey(Zajezdy, on_delete=models.CASCADE, db_column='trip_id')
    booking_date = models.DateField()
    people = models.IntegerField()
    cena = models.IntegerField()
    stav = models.CharField(max_length=15)
    platba = models.CharField(max_length=15)

    def __str__(self):
        return f"Rezervace {self.booking_id} - {self.customer.prijmeni}"

    class Meta:
        verbose_name_plural = "Rezervace"