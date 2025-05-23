from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Producto(models.Model):
    imagen = CloudinaryField('imagen', blank=True, null=True)
    nombre_producto = models.CharField(max_length=255)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre_producto

    class Meta:
        db_table = 'SunnyApp_producto'  # nombre exacto de la tabla en Supabase
        managed = False  # Django no creará ni modificará esta tabla