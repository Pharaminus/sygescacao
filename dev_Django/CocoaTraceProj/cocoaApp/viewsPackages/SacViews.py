from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from cocoaApp.models import Sac
from cocoaApp.serializer import SacSerializer


class SacListview(ListView):
    model = Sac
    
    template_name = 'cocoaApp/sac.html'
    
class SacCreateview(CreateView):
    model = Sac
    fields = ['code_qr','quantite', 'date_creation', 'date_modification', 'acheteur']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/sac'
    
class SacDeleteview(DeleteView):
    model = Sac
    template_name = 'cocoaApp/delete.html'
    success_url = '/sac'
class SacUpdateview(UpdateView):
    model = Sac
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/sac'
    
class SacViewset(viewsets.ModelViewSet):
    queryset = Sac.objects.all()
    serializer_class = SacSerializer