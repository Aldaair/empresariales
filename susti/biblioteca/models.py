from django.db import models

# Create your models here.

class Autor(models.Model):
    IdAutor = models.AutoField(primary_key=True)
    Nombre = models.TextField()
    Nacionalidad = models.TextField()
    def __str__(self):
        return self.Nombre
    class Meta:
        db_table = 'Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

class Libro(models.Model):
    IdLibro = models.AutoField(primary_key=True)
    Codigo = models.IntegerField()
    Titulo = models.TextField()
    ISBN = models.TextField()
    Editorial = models.TextField()
    NumPags = models.IntegerField()
    IdAutor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.Titulo
    class Meta:
        db_table = 'Libro'
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    NumUsuario = models.IntegerField()
    NIF = models.TextField()
    Nombre = models.TextField()
    Direccion = models.TextField()
    Telefono = models.TextField()
    def __str__(self):
        return self.Nombre
    class Meta:
        db_table = 'Usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
class Prestamos(models.Model):
    IdPrestamo = models.AutoField(primary_key=True)
    IdLibro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    FecPrestamo = models.DateField()
    FecDevolucion = models.DateField()
    def __str__(self):
        return str(self.IdPrestamo)
    class Meta:
        db_table = 'Prestamo'
        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'