from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models



class Uiu(models.Model):   
    oid = models.IntegerField(primary_key=True)
    foglio = models.IntegerField(null=True, blank=True)
    numero = models.CharField(max_length=15, blank=True)
    tipologia = models.CharField(max_length=50, blank=True)
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    ici_stato = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'uiu'
       
class Ppurbutm(models.Model):
    oid = models.IntegerField(primary_key=True)
    layer = models.CharField(max_length=254, blank=True)
    string = models.CharField(max_length=254, blank=True)
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    class Meta:
        db_table = 'ppurbutm'

class Psaiurbutm(models.Model):
    oid = models.IntegerField(primary_key=True)
    layer = models.CharField(max_length=50, blank=True)
    string = models.CharField(max_length=150, blank=True)
    norme = models.CharField(max_length=254, blank=True)
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    class Meta:
        db_table = 'psaiurbutm'

class Psdaurbutm(models.Model):
    oid = models.IntegerField(primary_key=True)
    layer = models.CharField(max_length=254, blank=True)
    string = models.CharField(max_length=254, blank=True)
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    class Meta:
        db_table = 'psdaurbutm'

class Ptpurbutm(models.Model):
    oid = models.IntegerField(primary_key=True)
    layer = models.CharField(max_length=254, blank=True)
    string = models.CharField(max_length=254, blank=True)    
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    class Meta:
        db_table = 'ptpurbutm'

class Sicurbutm(models.Model):
    oid = models.IntegerField(primary_key=True)
    tipologia = models.CharField(max_length=50, blank=True)
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    layer = models.CharField(max_length=20, blank=True)
    string = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = 'sicurbutm'

class Zpsurbutm(models.Model):
    oid = models.IntegerField(primary_key=True)
    layer = models.CharField(max_length=50, blank=True)
    objects =models.GeoManager()
    the_geom = models.PolygonField(srid=32633)
    string = models.CharField(max_length=60, blank=True)
    class Meta:
        db_table = 'zpsurbutm'