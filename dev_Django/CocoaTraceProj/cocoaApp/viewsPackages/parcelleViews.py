from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from cocoaApp.models import Parcelle
from cocoaApp.serializer import ParcelleSerializer


class ParcelleListview(ListView):
    model = Parcelle
    
    template_name = 'cocoaApp/Parcelle.html'
    
class ParcelleCreateview(CreateView):
    model = Parcelle
    fields = ['numero_titre_foncier','statut', 'coordonnees_polygonales', 'superficie', 'nombre_arbres', 'age_moyen_arbres', 'producteur']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/parcelle'
    
class ParcelleDeleteview(DeleteView):
    model = Parcelle
    template_name = 'cocoaApp/delete.html'
    success_url = '/parcelle'
class ParcelleUpdateview(UpdateView):
    model = Parcelle
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/parcelle'
    
class ParcelleViewset(viewsets.ModelViewSet):
    queryset = Parcelle.objects.all()
    serializer_class = ParcelleSerializer