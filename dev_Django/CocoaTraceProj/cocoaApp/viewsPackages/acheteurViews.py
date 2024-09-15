from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from cocoaApp.models import Acheteur
from cocoaApp.serializer import AcheteurSerializer


class AcheteurListview(ListView):
    model = Acheteur
    
    template_name = 'cocoaApp/acheteur.html'
    
class AcheteurCreateview(CreateView):
    model = Acheteur
    fields = ['nom','prenom', 'type_acheteur', 'numero_cni']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/acheteur'
    
class AcheteurDeleteview(DeleteView):
    model = Acheteur
    template_name = 'cocoaApp/delete.html'
    success_url = '/acheteur'
class AcheteurUpdateview(UpdateView):
    model = Acheteur
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/acheteur'
    
class AcheteurViewset(viewsets.ModelViewSet):
    queryset = Acheteur.objects.all()
    serializer_class = AcheteurSerializer