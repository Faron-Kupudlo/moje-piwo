from django.db import models

class wpis(models.Model):
    nazwa_piwa = models.CharField(max_length=50)
    surowce = models.TextField(max_length=500)
    drożdże = models.CharField(max_length=100)

    class fermentacja (models.TextChoices):
        rd = 'rd', ('rehydratyzacja drożdży')
        sd = 'sd', ('starter drożdżowy')

    fermentacja =models.CharField(max_length=30, choices=fermentacja.choices, default=fermentacja.rd)

    objetosc = models.IntegerField("objętość brzeczki w fermentatorze [litry]", max_length=2, default='20')
    temperatura_D_D = models.IntegerField("temperatura dodania drożdży [°C]", max_length=3, default='19')
    startowa_wartość_BLG = models.FloatField(max_length=5, null=True, blank=True, default='0')
    końcowa_wartość_BLG = models.FloatField(max_length=5, null=True, blank=True, default='0')
    # przebieg fermentacji burzliwej


