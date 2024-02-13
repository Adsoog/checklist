from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Persona(models.Model):
    persona_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class DesempenoDiario(models.Model):
    registro_id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE
    )  # Relación con Persona
    tarea_descripcion = models.CharField(max_length=100)
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    fecha = models.DateField(
        auto_now_add=True
    )  # Esta línea establece la fecha automáticamente al crear el registro

    def __str__(self):
        return f"{self.persona.nombre} - {self.tarea_descripcion} - {self.puntuacion}"
