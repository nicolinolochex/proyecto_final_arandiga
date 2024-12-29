from django.urls import path
from APP import views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    VehiculosClientesListView, 
    VehiculosClientesUpdateView, 
    VehiculosClientesDeleteView, 
    VehiculosClientesDetailView  # Asegúrate de incluir esto
)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),  # Asegúrate de que la vista formulario esté apuntando al formulario correcto
    path('acercade/', views.about, name='aboutv2'),
    path('base_clientes/', views.base_clientes, name='base_clientes'),
    path('publicar_cv/', views.publicar_cv, name='publicar_cv'),
    path('publicar_rodado/', views.publicar_rodado, name='publicar_rodado'),
    path('success/', views.success, name='success'),  # Esta es la URL para success
    path('buscar-vehiculo/', views.buscar_vehiculo, name="Buscar_Vehiculo"),
    path('tests/', views.tests, name="tests"),
    path('vehiculos/', VehiculosClientesListView.as_view(), name='vehiculos-list'),
    path('vehiculos/editar/<int:pk>/', VehiculosClientesUpdateView.as_view(), name='vehiculos-update'),
    path('vehiculos/eliminar/<int:pk>/', VehiculosClientesDeleteView.as_view(), name='vehiculos-delete'),
    path('no_permitido/', views.no_permitido, name='mensaje_no_permitido'),
    path('vehiculos/detalle/<int:pk>/', VehiculosClientesDetailView.as_view(), name='vehiculo-detail'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)