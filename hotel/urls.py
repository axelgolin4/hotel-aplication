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



    ]
