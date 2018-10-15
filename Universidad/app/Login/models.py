from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

User = get_user_model()


class Alumno(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    carnet = models.CharField(max_length=10)
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')

    def NombreAlumno(self):
        return "{0} {1}, {2}".format(self.nombre, self.apellido, self.carnet)

    def __str__(self):
        return self.NombreAlumno()


class Carrera(models.Model):

    nombrecarrera = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{0} ({1})" .format(self.nombrecarrera, self.precio)


class Matriculacion(models.Model):

    Alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(default=timezone.now(), editable=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.alumno, self.Carrera.nombre)