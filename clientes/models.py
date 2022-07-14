from django.db import models


class Cliente(models.Model):
    idCliente = models.CharField(max_length=50 )
    nombre = models.CharField(max_length=50)
    apellidoPaterno = models.CharField(max_length=50)
    apellidoMaterno = models.CharField(max_length=50)
    fechaNacimiento = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    segmento = models.SmallIntegerField()
    nacionalidad = models.CharField(max_length=50)
    rfc = models.CharField(max_length=50)
    tipoID = models.CharField(max_length=50)
    cuenta = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    # TDD = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre