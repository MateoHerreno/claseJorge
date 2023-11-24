from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion_categoria']
    search_fields = ['nombre']
    
@admin.register(Productos)
class Producto(admin.ModelAdmin):
    list_display = ['id','nombre','Precio','descripcion_producto','cantidad','fecha_Creacion','categoria']
    search_fields = ['nombre']
    
@admin.register(Servicios)
class Servicio(admin.ModelAdmin):
    list_display = ['id','nombre','Precio','descripcion_servicio','categoria']
    search_fields = ['nombre']
    
@admin.register(Empleado)
class Empleado(admin.ModelAdmin):
    list_display = ['id','nombre_completo','cedula','correo','telefono','fecha_contratacion','cargo']
    search_fields = ['nombre']
    
@admin.register(Clientes)
class Cliente(admin.ModelAdmin):
    list_display = ['id','nombre_completo','cedula','correo','telefono','direccion']
    search_fields = ['nombre']
    
    
@admin.register(Proveedores)
class Proveedore(admin.ModelAdmin):
    list_display = ['id','nombre','nit','telefono','correo']
    search_fields = ['nombre']
    
@admin.register(Usuarios)
class Usuario(admin.ModelAdmin):
    list_display=['id','nombre','correo','clave','rol']
    search_fields = ['nombre']