from django.db import models


class Parking(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    @property
    def total_places(self):
        return Place.objects.filter(section__in=Section.objects.filter(parking=self)).count()


class Section(models.Model):
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    @property
    def total_places(self):
        return Place.objects.filter(section=self).count()


class Place(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    place_status = models.IntegerField(null=True, blank=True)
    device_id = models.IntegerField(unique=True, default=None)




