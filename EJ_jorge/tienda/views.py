from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Importamos todos los modelos de la base de datos
from .models import *

# Create your views here.
def index(request):
	return render(request, "tienda/login/login.html")


def inicio(request):
	return render(request, "tienda/inicio.html")


def categorias(request):
	# SELECT * FROM categoria
	q = Categoria.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/categorias/categorias.html", contexto)


def categorias_form(request):
	return render(request, "tienda/categorias/categorias_form.html")


def categorias_crear(request):
	if request.method == "POST":
		nomb = request.POST.get("nombre")
		desc = request.POST.get("descripcion")
		try:
			q = Categoria(
				nombre=nomb,
				descripcion=desc
			)
			q.save()
			messages.success(request, "Guardado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
		return redirect("categorias_listar")

	else:
		messages.warning(request, "Error: No se enviaron datos...")
		return redirect("categorias_listar")


def categorias_eliminar(request, id):
	try:
		q = Categoria.objects.get(pk=id)
		q.delete()
		messages.success(request, "Categoría eliminada correctamente!!")
	except Exception as e:
		messages.error(request, f"Error: {e}")

	return redirect("categorias_listar")


def categorias_formulario_editar(request, id):
	q = Categoria.objects.get(pk=id)
	contexto = {"data": q}
	return render(request, "tienda/categorias/categorias_formulario_editar.html", contexto)

def categorias_actualizar(request):
	if request.method == "POST":
		id = request.POST.get("id")
		nomb = request.POST.get("nombre")
		desc = request.POST.get("descripcion")
		try:
			q = Categoria.objects.get(pk=id)
			q.nombre = nomb
			q.descripcion = desc
			q.save()
			messages.success(request, "Categoría actualizada correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("categorias_listar")


def productos(request):
	q = Producto.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/productos/productos.html", contexto)


def productos_form(request):
	q = Categoria.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/productos/productos_form.html", contexto)


def productos_crear(request):
	if request.method == "POST":
		nombre = request.POST.get("nombre")
		precio = request.POST.get("precio")
		inventario = request.POST.get("inventario")
		fecha_creacion = request.POST.get("fecha_creacion")
		categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Producto(
				nombre=nombre,
				precio=precio,
				inventario=inventario,
				fecha_creacion=fecha_creacion,
				categoria=categoria
			)
			q.save()
			messages.success(request, "Guardado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
		return redirect("productos_listar")

	else:
		messages.warning(request, "Error: No se enviaron datos...")
		return redirect("productos_listar")


def productos_eliminar(request, id):
	try:
		q = Producto.objects.get(pk=id)
		q.delete()
		messages.success(request, "Producto eliminada correctamente!!")
	except Exception as e:
		messages.error(request, f"Error: {e}")

	return redirect("productos_listar")


def productos_formulario_editar(request, id):
	q = Producto.objects.get(pk=id)
	c = Categoria.objects.all()
	contexto = {"data": q, "categoria": c}
	return render(request, "tienda/productos/productos_formulario_editar.html", contexto)

def productos_actualizar(request):
	if request.method == "POST":
		id = request.POST.get("id")
		nombre = request.POST.get("nombre")
		precio = request.POST.get("precio")
		inventario = request.POST.get("inventario")
		fecha_creacion = request.POST.get("fecha_creacion")
		categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Producto.objects.get(pk=id)
			q.nombre = nombre
			q.precio = precio
			q.inventario = inventario
			q.fecha_creacion = fecha_creacion
			q.categoria = categoria
			q.save()
			messages.success(request, "Producto actualizado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("productos_listar")

