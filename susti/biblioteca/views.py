from django.shortcuts import render
from .models import Autor, Libro, Prestamos, Usuario
# Create your views here.


def index(request):
    listAutor = Autor.objects.all()
    listLibro = Libro.objects.all()
    listPrestamos = Prestamos.objects.all()
    listUsuario = Usuario.objects.all()

    context = {
        'listAutor': listAutor,
        'listLibro': listLibro,
        'listPrestamos': listPrestamos,
        'listUsuario': listUsuario,
    }
    return render(request, 'gestion.html', context)
