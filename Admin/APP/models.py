from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.email})"

from django.db import models

class VehiculosClientes(models.Model):
    UNIDAD_CHOICES = [
        ('Car', 'Car'),
        ('Truck', 'Truck'),
        ('Motorcycle', 'Motorcycle'),
        # Puedes agregar más opciones según lo necesites
    ]
    
    unidad = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)  # Puede ser el modelo y año, como "Toyota Corolla 2020"
    kilometraje = models.IntegerField()  # En kilómetros
    precio_usd = models.DecimalField(max_digits=10, decimal_places=2)  # Precio en USD
    foto = models.ImageField(upload_to='vehiculos_pics/', blank=True, null=True)  # Imagen del vehículo
    
    # Definir una función __str__ para una representación legible
    def __str__(self):
        return f"{self.unidad} - {self.modelo} ({self.kilometraje} km)"

    
    # Crear el modelo TrabajaConNosotros
class TrabajaConNosotros(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    curriculum = models.FileField(upload_to='curriculums/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.email})"