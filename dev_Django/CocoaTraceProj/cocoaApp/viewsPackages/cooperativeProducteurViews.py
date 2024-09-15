from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from cocoaApp.models import CooperativeProducteur
from cocoaApp.serializer import CooperativeProducteurSerializer


class CooperativeProducteurListview(ListView):
    model = CooperativeProducteur
    template_name = 'cocoaApp/cooperativeProducteur.html'
    
    
    
class CooperativeProducteurCreateview(CreateView):
    model = CooperativeProducteur
    fields = ['date_arriver_producteur','cooperative', 'producteur']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/cooperativeProducteur'
    
class CooperativeProducteurDeleteview(DeleteView):
    model = CooperativeProducteur
    template_name = 'cocoaApp/delete.html'
    success_url = '/cooperativeProducteur'
class CooperativeProducteurUpdateview(UpdateView):
    model = CooperativeProducteur
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/cooperativeProducteur'
    
class CooperativeProducteurViewset(viewsets.ModelViewSet):
    queryset = CooperativeProducteur.objects.all()
    serializer_class = CooperativeProducteurSerializer