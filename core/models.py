from django.db import models

from django.contrib.gis.db import models

class Shapefile(models.Model):
    name = models.CharField(max_length=100)
    geometry = models.MultiPolygonField()

    def __str__(self):
        return self.name

