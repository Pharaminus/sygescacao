from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from rest_framework import viewsets

from cocoaApp.models import Cooperative, Producteur, CooperativeProducteur
from cocoaApp.serializer import CooperativeSerializer


class CooperativeListview(ListView):
    
    model = Cooperative
    
    template_name = 'cocoaApp/cooperative.html'
    
class CooperativeCreateview(CreateView):
    model = Cooperative
    fields = ['numero_titre_foncier','statut', 'coordonnees_polygonales', 'superficie', 'nombre_arbres', 'age_moyen_arbres', 'producteur']
    template_name = 'cocoaApp/newpost.html'
    success_url = '/cooperative'
    
class CooperativeDeleteview(DeleteView):
    model = Cooperative
    template_name = 'cocoaApp/delete.html'
    success_url = '/cooperative'
class CooperativeUpdateview(UpdateView):
    model = Cooperative
    fields = '__all__'
    template_name = 'cocoaApp/newpost.html'
    success_url = '/cooperative'
    
class CooperativeViewset(viewsets.ModelViewSet):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer

def loginCooperative(request):
    if request.method == 'POST':
        identifiant = request.POST.get('identifiant')
        mot_pass = request.POST.get('mot_pass')
        print(f"=========| pass 1 {identifiant}=={mot_pass}")
        if Cooperative.objects.filter(identifiant_unique=identifiant, mot_pass=mot_pass):
            print("=========| pass 2")
            
            return render(request, 'cocoaApp/cooperative.html')
        
    return render(request, 'cocoaApp/cooperativelogin.html')
    
        