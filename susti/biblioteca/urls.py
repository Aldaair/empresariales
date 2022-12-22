from django.urls import path
from . import views
urlpatterns = [
    path('listado/', views.index , name='info'),
]