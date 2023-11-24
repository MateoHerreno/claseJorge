from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages

# crud de  productos.
def index(request):
    return render(request, "tienda/index.html")

def listarProductos(request):
    q = Productos.objects.all()
    contexto = {"data":q}
    return render(request, "tienda/productos/listarProductos.html",contexto)

def editarProductos(request, id):
	q = Productos.objects.get(pk=id)
	c = Categoria.objects.all()
	contexto = {"data": q, "categoria": c}
	return render(request, "tienda/productos/editarProductos.html", contexto)

def actualizarProductos(request):
	if request.method == "POST":
		id = request.POST.get("id")
		nombre = request.POST.get("nombre")
		Precio = request.POST.get("precio")
		descripcion_producto = request.POST.get("descripcion")
		cantidad = request.POST.get("cantidad")
		fecha_Creacion = request.POST.get("fecha_creacion")
		categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Productos.objects.get(pk=id)
			q.nombre = nombre
			q.Precio = Precio
			q.descripcion_producto = descripcion_producto
			q.cantidad = cantidad
			q.fecha_Creacion = fecha_Creacion
			q.categoria = categoria
			q.save()
			messages.success(request, "Producto actualizado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("listarProductos")

def eliminarProductos(request, id):
	try:
		q = Productos.objects.get(pk=id)
		q.delete()
		messages.success(request, "Eliminado, Exitosamiente!")
	except Exception as e:
		messages.error(request, f"Error: {e}")
        
	return redirect("listarProductos")

def crearProductoform(request):
	q = Categoria.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/productos/crearProductoform.html", contexto)

def crearProducto(request):
	if request.method == "POST":
		nombre = request.POST.get("nombre")
		Precio = request.POST.get("precio")
		descripcion_producto = request.POST.get("descripcion")
		cantidad = request.POST.get("cantidad")
		fecha_Creacion = request.POST.get("fecha_Creacion")
		categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Productos(
                nombre = nombre,
                Precio = Precio,
                descripcion_producto = descripcion_producto,
                cantidad = cantidad,
                fecha_Creacion = fecha_Creacion,
                categoria = categoria
			)
			q.save()
			messages.success(request, "Guardado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
		return redirect("listarProductos")

	else:
		messages.warning(request, "Error: No se enviaron datos...")
		return redirect("listarProductos")

#crud de clientes

def registrarCliente(request):
    return render(request, "tienda/clientes/registrarCliente.html")

def listarCliente(request):
    q = Clientes.objects.all()
    contexto = {"data" : q}
    return render(request, "tienda/clientes/listarCliente.html",contexto)

def clientesCrear(request):
    if request.method == 'POST':
        cedula=request.POST.get('cedula')        
        nombre=request.POST.get('nombre_completo')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')

        try:
            q = Clientes(
                cedula=cedula,
                nombre_completo=nombre,
                correo=correo,
                telefono=telefono
            )
            q.save()
            messages.success(request,"Guardado Correctamente!")
        except Exception as e:
            messages.error(request,f"Error:{e}")
        return redirect('listarCliente')

    else:
        messages.error(request,"Error: no se enviaron datos")
        return redirect("listarCliente")

def clientesEliminar(request,id):
    try:
        q = Clientes.objects.get(pk = id)
        q.delete()
        messages.success(request,"Cliente eliminado Correctamente!")
    except Exception as e:
        messages.error(request,f"Error:{e}")
    return redirect('listarCliente')

def clientesEditar(request,id):
    q = Clientes.objects.get(pk = id)
    contexto = {"data" : q}
    return render(request,"tienda/clientes/editarCliente.html",contexto)

def clientesActualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        cedula=request.POST.get('cedula')        
        nombre_completo=request.POST.get('nombre_completo')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')
        try:
            q=Clientes.objects.get(pk=id)
            q.cedula = cedula
            q.nombre_completo = nombre_completo
            q.correo = correo
            q.telefono = telefono
            q.save()
            messages.success(request, "Cliente actualizado correctamente!!")
        except Exception as e:
            messages.error(request,f"ERROR:{e}")
        return redirect("listarCliente")
    else:
        messages.error(request,"Error: no se enviaron datos")
        return redirect("listarCliente")
        
#Crud empleados
def empleados(request):
	# SELECT * FROM categoria
	q = Empleado.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/empleados/listarempleados.html", contexto)

def nuevoempleado(request):
	return render(request, "tienda/empleados/crearempleado.html")

def newempleado(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        fechac = request.POST.get('fecha')
        cargo = request.POST.get('cargo')
        try:
            q = Empleado(
                nombre_completo = nombre,
                cedula = cedula,
                correo = correo,
                telefono = telefono,
                fecha_contratacion = fechac,
                cargo = cargo
            )
            q.save()
            messages.success(request, 'guardado correctamente')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return redirect('empleado')

def empleados_formulario_editar(request, id):
	q = Empleado.objects.get(pk=id)
	c = Empleado.objects.all()
	contexto = {"data": q, "empleado": c}
	return render(request, "tienda/empleados/editarempleados.html", contexto)


def empleado_actualizar(request):
	if request.method == "POST":
		id = request.POST.get("id")
		nombre = request.POST.get("nombre")
		cedula = request.POST.get("cedula")
		correo = request.POST.get("correo")
		telefono = request.POST.get("telefono")
		cargo = request.POST.get("cargo")
		try:
			q = Empleado.objects.get(pk=id)
			q.nombre_completo = nombre
			q.cedula = cedula
			q.correo = correo
			q.telefono = telefono
			q.cargo = cargo
			q.save()
			messages.success(request, "Producto actualizado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("empleado")

def empleado_eliminar(request, id):
	try:
		q = Empleado.objects.get(pk=id)
		q.delete()
		messages.success(request, "Producto eliminada correctamente!!")
	except Exception as e:
		messages.error(request, f"Error: {e}")

	return redirect("empleado")

#crud proveedores
def proveedores_registrar(request):
	return render(request, "tienda/proveedores/registrarProveedor.html")

def listar_proveedores(request):
	# SELECT * FROM categoria
	q = Proveedores.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/proveedores/listarProveedor.html", contexto)


def proveedores_add(request):
	if request.method == "POST":
            nombre = request.POST.get("nombre")
            nit  = request.POST.get("nit")
            correo = request.POST.get("correo")
            tele = request.POST.get("tele")
            q = Proveedores(
                nombre =  nombre,
                correo = correo,
                nit = nit,
                telefono = tele,
        
            )
            q.save()
            messages.success(request, "Guardado correctamente!!")
            return redirect("listarProveedores")
        
def registrar_proveedores_editar(request,id):
    q = Proveedores.objects.get(pk=id)
    contexto = {"data": q}
    return render(request,"tienda/proveedores/registrarProveedorEditar.html",contexto)


def proveedores_actualizar(request):
        if request.method == "POST":
            id = request.POST.get("id")
            nombre = request.POST.get("nombre")
            nit  = request.POST.get("nit")
            correo = request.POST.get("correo")
            tele = request.POST.get("tele")
            try:
                q = Proveedores.objects.get(pk=id)
                q.nombre = nombre
                q.nit = nit
                q.correo = correo
                q.telefono = tele
                q.save() 
                messages.success(request,"Proveedor actualizada correctamente!!")
            except Exception as e:
                messages.error(request,f'Error: {e}')
        else:
            messages.warning(request,f'Error:No se enviaron los datos!!')
        return redirect('listarProveedores')

def proveedores_delete(request,id):
    try:
        q = Proveedores.objects.get(pk=id)
        q.delete()
        messages.success(request,"Proveedores eliminada correctamente!!!")
    except Exception as e:
        messages.error(request,f'Error:{e}')
    return redirect('listarProveedores')
