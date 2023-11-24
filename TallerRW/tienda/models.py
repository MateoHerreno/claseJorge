from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=254) 
    descripcion_categoria = models.TextField()
    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    nombre=models.CharField(max_length=254,unique=True)
    Precio=models.IntegerField()
    descripcion_producto = models.TextField()
    cantidad=models.IntegerField()
    fecha_Creacion=models.DateField()
    categoria=models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre
    
class Servicios(models.Model):
    nombre=models.CharField(max_length=254,unique=True)
    Precio=models.IntegerField()
    descripcion_servicio = models.TextField()
    categoria=models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre_completo=models.CharField(max_length=254)
    cedula=models.IntegerField(unique=True)
    correo=models.CharField(max_length=254,unique=True)
    telefono=models.IntegerField(unique=True)
    fecha_contratacion=models.DateField()
    cargo=models.CharField(max_length=254)
    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    nombre_completo=models.CharField(max_length=254)
    cedula=models.IntegerField(unique=True)
    correo=models.CharField(max_length=254,unique=True)
    telefono=models.IntegerField(unique=True)
    direccion=models.CharField(max_length=254)
    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    nombre=models.CharField(max_length=254)
    nit=models.IntegerField(unique=True)
    telefono=models.IntegerField(unique=True)
    correo=models.CharField(max_length=254,unique=True)
    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre=models.CharField(max_length=254)
    correo=models.CharField(max_length=254,unique=True)
    clave=models.CharField(max_length=254)
    ROLES = (
        (1, "administrador"),
        (2,"gerente"),
        (3,"empleado"),
        (4,"cliente"), 
    )
    rol=models.IntegerField(choices=ROLES,default=4)
    def __str__(self):
        return self.nombre