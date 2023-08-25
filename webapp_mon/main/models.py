from django.db import models

# Create your models here.

class get_professors(models.Model):
    Nombre_Completo = models.CharField(max_length=250)
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Ultima_Conexion = models.CharField(max_length=100)
    Dias_no_conexion = models.CharField(max_length=50)
    Foto_perfil = models.CharField(max_length=10)
    Presentacion_Docente = models.CharField(max_length=10)
    Fecha_Informe = models.CharField(max_length=100)
    Correo = models.CharField(max_length=50)

