from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class wpis(models.Model):
    nazwa_piwa = models.CharField(default='' , max_length=50)
    surowiec_1 = models.CharField('', default='',max_length=50, blank=True)
    surowiec_1_ilosc = models.FloatField('', default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)], blank=True)
    class jednostka (models.TextChoices):
        l = 'l', ('litr')
        g = 'g', ('gram')
        kg = 'kg', ('kilogram')

    surowiec_1_jednostka = models.CharField('', max_length=10, choices=jednostka.choices, default=jednostka.l, blank=True)
    surowiec_2 = models.CharField('', default='', max_length=50, blank=True)
    surowiec_2_ilosc = models.FloatField('', default=0,
                                         validators=[MaxValueValidator(1000000), MinValueValidator(0)], blank=True)
    surowiec_2_jednostka = models.CharField('', max_length=10, choices=jednostka.choices, default=jednostka.l,
                                            blank=True)
    surowiec_3 = models.CharField('', default='', max_length=50, blank=True)
    surowiec_3_ilosc = models.FloatField('', default=0,
                                         validators=[MaxValueValidator(1000000), MinValueValidator(0)], blank=True)
    surowiec_3_jednostka = models.CharField('', max_length=10, choices=jednostka.choices, default=jednostka.l,
                                            blank=True)
    drożdże = models.CharField(max_length=100)

    class fermentacja (models.TextChoices):
        rd = 'rd', ('rehydratyzacja drożdży')
        sd = 'sd', ('starter drożdżowy')

    fermentacja =models.CharField(max_length=30, choices=fermentacja.choices, default=fermentacja.rd)

    objetosc = models.FloatField('objętość w fermentatorze', default=20, validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    temperatura_D_D = models.FloatField('temperatura dodania drożdży', default=19, validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    startowa_wartość_BLG = models.FloatField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)])
    końcowa_wartość_BLG = models.FloatField(default=0, validators=[MaxValueValidator(1000000), MinValueValidator(0)])

    def __str__(self):
        return self.nazwa_piwa

    def get_absolute_url(self):
        return reverse('index')