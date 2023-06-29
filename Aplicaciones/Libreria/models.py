from django.db import models

""" Creamos el modelo ORM Usuario """
""" --------------- Gonzalo Quiroga -------------- """
class Libro(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    precio = models.PositiveSmallIntegerField()
    genero = models.CharField(max_length=50)
   

    """ Sobreescribimos la funcion __str__ para visualizar el contenido de la BD en la app de Django """
    def __str__(self):
        texto = "{0} | {1} | {2} | {3} | {4} | {5} | ({6})"
        return texto.format(self.nombre, self.autor, self.precio, self.genero, self.codigo)
