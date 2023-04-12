from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('inventario', views.inventario, name = 'inventario'),
    

    path('inventario_insumos', views.listar_insumos, name = 'listar_insumos'),
    path('editar_insumos/<id>', views.editar_insumos, name = 'editar_insumos'),
    path('eliminar_insumos/<id>', views.eliminar_insumos, name = 'eliminar_insumos'),
    path('registrar_entrada', views.Insumos_view, name = 'registrar_entrada'),
    path('registrar_salida', views.registrar_salida, name = 'registrar_salida'),



    path('inventario_blancos', views.listar_blancos, name = 'listar_blancos'),
    path('registrar_entradab', views.Blancos_view, name = 'Blancos_view'),
    path('registrar_salidab', views.registrar_salida, name = 'registrar_salida'),
    path('editar_blancos/<id>', views.editar_blancos, name = 'editar_blancos'),
    path('eliminar_blancos/<id>', views.eliminar_blancos, name = 'eliminar_blancos'),




    path('inventario_cocina', views.listar_cocina, name = 'listar_cocina'),
    path('registrar_entradac', views.Cocina_view, name = 'Cocina_view'),
    path('registrar_salidac', views.registrar_salida, name = 'registrar_salida'),
    path('editar_cocina/<id>', views.editar_cocina, name = 'editar_cocina'),
    path('eliminar_cocina/<id>', views.eliminar_cocina, name = 'eliminar_cocina'),
]
