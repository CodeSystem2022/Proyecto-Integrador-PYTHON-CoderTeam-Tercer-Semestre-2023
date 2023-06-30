
from django.shortcuts import render,redirect
from .models import Libro
from django.contrib import messages

# Create your views here.
""" Definimos y creamos nuestras vistas """
"""------------ Veronica Cardenas -----------"""
def home(request):
    libros = Libro.objects.all()
    messages.success(request,'Libros Listados!')
    return render(request, "gestionCRUD.html",{"libros":libros})


def registrarLibro(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    autor=request.POST['txtAutor']
    precio=request.POST['precio']
    genero=request.POST['genero']
   
    libro = Libro.objects.create(nombre=nombre,autor=autor,codigo=codigo,precio=precio,genero=genero) 
    messages.success(request,'Libro Registrado!')

    return redirect('/')

def eliminarLibro(request,codigo):
    libro = Libro.objects.get( codigo=codigo )
    libro.delete()
    messages.success(request,'Libro Eliminado!')
    
    return redirect('/')

def edicionLibro(request,codigo):
    libro = Libro.objects.get(codigo = codigo)

    return render(request, "edicionLibro.html",{"libro":libro})

def editarLibro(request):
    codigo =request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    autor=request.POST['txtAutor']
    precio=request.POST['precio']
    genero=request.POST['genero']

    
    libro = Libro.objects.get(codigo = codigo)

    libro.nombre=nombre
    libro.autor=autor
    libro.precio=precio
    libro.genero=genero

    libro.save()
    messages.success(request,'Libro Actualizado!')

    return redirect('/')
