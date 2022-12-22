from django.contrib import admin
from .models import Autor, Libro, Prestamos, Usuario
# Register your models here.

admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Prestamos)
admin.site.register(Usuario)
