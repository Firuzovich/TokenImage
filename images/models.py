from django.db import models
from django.utils import timezone

class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'images_region'

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, related_name='districts', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images_district'
        unique_together = ('name', 'region')  # Region bilan birgalikda tuman nomi unikal bo'lishi kerak

    def __str__(self):
        return f'{self.name} ({self.region.name})'

class BarcodeData(models.Model):
    barcode = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    fish = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'{self.barcode} - {self.fish}'
