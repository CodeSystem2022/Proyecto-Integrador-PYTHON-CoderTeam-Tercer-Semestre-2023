from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('registrarCurso/', views.registrarCurso),
  path('edicionCurso/', views.edicionCurso),
  path('editarCursos/', views.editarCurso),
  path('eliminarCurso/', views.eliminarCurso)
]
