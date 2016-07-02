from django.contrib import admin
from deudas.models import Deudore, Deuda


class DeudoreAdmin(admin.ModelAdmin):
    #list_display = ('name','rut','status','apellido_paterno','apellido_materno','estado_Civil','fecha_nacimiento')
    pass

class DeudaAdmin(admin.ModelAdmin):
    #list_display = ('name','acreedor','descripcion','deudor','status','fecha_inicio','monto','created_at','update_at')    
    pass

admin.site.register(Deuda, DeudaAdmin)
admin.site.register(Deudore, DeudoreAdmin)