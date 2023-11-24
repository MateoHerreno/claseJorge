from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    #crud de productos
    path('listarProductos',views.listarProductos, name = "listarProductos"),
    path("editarProductos/<int:id>", views.editarProductos, name="editarProductos"),
    path("actualizarProductos/", views.actualizarProductos, name="actualizarProductos"),
    path("eliminarProductos/<int:id>", views.eliminarProductos, name="eliminarProductos"),
    path("crearProductoform/", views.crearProductoform, name="crearProductoform"),
	path("crearProducto/", views.crearProducto, name="crearProducto"),
    
    #Crud empleados
    path("empleados/", views.empleados, name="empleado"),
    path("nuevoempleados/", views.nuevoempleado, name="nuevoempleados"),
    path("newempleados/", views.newempleado, name="newempleados"),
    path("empleados_formulario_editar/<int:id>", views.empleados_formulario_editar, name="empleados_formulario_editar"),
    path("empleado_actualizar/", views.empleado_actualizar, name="empleado_actualizar"),
    path("empleado_eliminar/<int:id>", views.empleado_eliminar, name="empleado_eliminar"),
    
    #Crud de clientes
    path('registrarCliente/',views.registrarCliente, name="registrarCliente"),
    path('listarCliente/',views.listarCliente, name="listarCliente"),
    path('clientesCrear/',views.clientesCrear, name="clientesCrear"),
    path('clientesEditar/<int:id>',views.clientesEditar, name="clientesEditar"),
    path('clientesEliminar/<int:id>',views.clientesEliminar, name="clientesEliminar"),
    path('clientesActualizar/',views.clientesActualizar, name="clientesActualizar"),
    
    #crud de proveedores
    path("registrarProveedores", views.proveedores_registrar, name="registrarProveedores"),
    path("listarProveedores/", views.listar_proveedores, name="listarProveedores"),
    path("addProveedores/", views.proveedores_add, name="proveedores_form"),
    path("proveedos_editar/<int:id>", views.registrar_proveedores_editar, name="proveedores_form_act"),
    path("proveedores_actualizar/", views.proveedores_actualizar, name="proveedores_actualizar"),
    path("deleteProveedores/<int:id>", views.proveedores_delete, name="proveedores_delete"),
]
