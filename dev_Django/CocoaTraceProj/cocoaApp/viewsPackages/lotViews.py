from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from cocoaApp.models import Lot
from cocoaApp.serializer import LotSerializer


class LotListview(ListView):
    model = Lot
    
    template_name = 'cocoaApp/lot.html'
    
class LotCreateview(CreateView):
    model = Lot
    fields = ['numero_lot','quantite', 'type_commercial', 'taux_humidite', 'date_recolt', 'date_livraison', 'cooperative', 'producteur', 'sac', 'parcelle']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/lot'
    
class LotDeleteview(DeleteView):
    model = Lot
    template_name = 'cocoaApp/delete.html'
    success_url = '/lot'
class LotUpdateview(UpdateView):
    model = Lot
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/lot'
    
class LotViewset(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer