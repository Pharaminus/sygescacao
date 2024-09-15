from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from cocoaApp.models import Producteur, CooperativeProducteur
from cocoaApp.serializer import ProducteurSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

class ProducteurListview(ListView):
    model = Producteur
    template_name = 'cocoaApp/producteur.html'
    context_object_name = 'producteurs'
    login_url = 'logincooperative'

    def get_queryset(self):
        # cooperative_id = self.kwargs['cooperative_id']  # Récupérer l'ID de la coopérative depuis les paramètres d'URL
        cooperative_id = self.request.GET.get('cooperative_id') 
        if cooperative_id:
            return Producteur.objects.filter(producteurCoop__cooperative_id=cooperative_id)
        return Producteur.objects.all()
    
    
    


class ProducteurCreateview(CreateView, LoginRequiredMixin):
    model = Producteur
    fields = ['identifiant_unique','nom', 'prenom', 'date_naissance', 'lieu_naissance', 'genre', 'numero_cni', 'identifiant_fodecc_cicc', 'numero_telephone', 'region', 'departement', 'arrondissement', 'village']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/producteur'
    
class ProducteurDeleteview(DeleteView):
    model = Producteur
    template_name = 'cocoaApp/delete.html'
    success_url = '/producteur'
class ProducteurUpdateview(UpdateView):
    model = Producteur
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/producteur'

# @login_required
class ProducteurViewset(viewsets.ModelViewSet, LoginRequiredMixin):
    queryset = Producteur.objects.all()
    serializer_class = ProducteurSerializer
    
