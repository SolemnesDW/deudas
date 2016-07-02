from __future__ import unicode_literals

from django.db import models

class Deudore(models.Model):
    rut = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=200)
    apellido_materno = models.CharField(max_length=200)
    estado_Civil = models.CharField(max_length=200)
    fecha_nacimiento = models.DateTimeField()
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Deuda(models.Model):
    name = models.CharField(max_length=100)
    acreedor = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='images/data',blank=True,null=True)
    description = models.TextField()
    fehca_inicio = models.DateTimeField()
    monto = models.IntegerField(default=0)
    #sku = models.CharField(max_length=100,unique=True)
    #price = models.DecimalField(max_digits=11, decimal_places=2)
    Deudore = models.ForeignKey(Deudore)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name