from django.db import models


class Destinace(models.Model):
    destination_id = models.AutoField(primary_key=True)
    nazev = models.CharField(max_length=80, verbose_name="Název destinace")
    zeme = models.CharField(max_length=80, verbose_name="Země")

    def __str__(self):
        return f"{self.nazev} ({self.zeme})"

    class Meta:
        db_table = "destinace"
        verbose_name = "Destinace"
        verbose_name_plural = "Destinace"


class Zajezdy(models.Model):
    trip_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="Název zájezdu")
    zacatek = models.DateField(verbose_name="Začátek zájezdu")
    konec = models.DateField(verbose_name="Konec zájezdu")
    cena = models.IntegerField(verbose_name="Cena v Kč")
    destination = models.ForeignKey(
        Destinace,
        on_delete=models.CASCADE,
        db_column="destination_id",
        verbose_name="Destinace"
    )
    kapacita = models.IntegerField(default=20, verbose_name="Kapacita")
    obsazeno = models.IntegerField(default=0, verbose_name="Obsazeno")
    doprava = models.CharField(max_length=30, verbose_name="Doprava")
    typ_dovolene = models.CharField(
        max_length=20,
        db_column="typy_dovolene",
        verbose_name="Typ dovolené"
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "zajezdy"
        verbose_name = "Zájezd"
        verbose_name_plural = "Zájezdy"


class Zakaznici(models.Model):
    customer_id = models.AutoField(primary_key=True)
    jmeno = models.CharField(max_length=50, verbose_name="Jméno")
    prijmeni = models.CharField(max_length=50, verbose_name="Příjmení")
    email = models.EmailField(max_length=100, verbose_name="Email")
    telefon = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon")
    ulice = models.CharField(max_length=50, blank=True, null=True)
    cp = models.CharField(max_length=10, db_column="č.p.", blank=True, null=True)
    mesto = models.CharField(max_length=40, blank=True, null=True, verbose_name="Město")
    psc = models.CharField(max_length=10, db_column="psč", blank=True, null=True)
    stat = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

    class Meta:
        db_table = "zakaznici"
        verbose_name = "Zákazník"
        verbose_name_plural = "Zákazníci"


class Rezervace(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(
        Zakaznici,
        on_delete=models.CASCADE,
        db_column="customer_id",
        verbose_name="Zákazník"
    )
    trip = models.ForeignKey(
        Zajezdy,
        on_delete=models.CASCADE,
        db_column="trip_id",
        verbose_name="Zájezd"
    )
    booking_date = models.DateField(verbose_name="Datum rezervace")
    people = models.IntegerField(default=1)
    cena = models.IntegerField()
    stav = models.CharField(max_length=15, default="Čeká na platbu")
    platba = models.CharField(max_length=15, default="Nezaplaceno")
    poznamka = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Rezervace č. {self.booking_id}"

    class Meta:
        db_table = "rezervace"
        verbose_name = "Rezervace"
        verbose_name_plural = "Rezervace"