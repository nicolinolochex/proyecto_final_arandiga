from django.contrib import admin
from APP.models import Contact

# Personalización del modelo Contact para el admin
class ContactAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista
    list_display = ('name', 'email', 'phone', 'message')
    # Campos por los cuales se podrá buscar
    search_fields = ('name', 'email', 'phone')
    # Opciones de filtro
    list_filter = ('email',)

# Registro del modelo con la configuración personalizada
admin.site.register(Contact, ContactAdmin)
