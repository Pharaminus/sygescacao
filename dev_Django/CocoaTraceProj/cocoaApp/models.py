from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# ====| tutoriel pour l'API REST |=======
class Blog(models.Model):
    topic = models.CharField(max_length=200)
    body = models.TextField()
#Your Model Identity
    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")
    def __str__(self):
        return self.topic
    
    
class User(AbstractUser, models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('adminCoop', 'AdminCoop'),
        ('acteur', 'Acteur'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='acteur')

    def __str__(self):
        return self.username
    
class Acheteur(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    type_acheteur = models.CharField(max_length=200)
    numero_cni = models.CharField(max_length=200)
    numero_oncc = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    filiale = models.CharField(max_length=200)
    coordonnees_geographiques = models.CharField(max_length=200)
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'acheteur'
        verbose_name_plural = 'acheteurs'
    def __str__(self):
        return self.nom
    

class Sac(models.Model):
    '''Model definition for Sac.'''
    
    code_qr = models.CharField(max_length=200)
    quantite = models.FloatField(null=True)
    date_creation = models.DateField()
    date_modification = models.DateField()
    acheteur = models.ForeignKey(Acheteur, related_name='acheteur', on_delete=models.CASCADE)
    class Meta:
        '''Meta definition for Sac.'''

        verbose_name = 'Sac'
        verbose_name_plural = 'Sacs'

    def __str__(self):
        pass


class Producteur(models.Model):
    '''Model definition for Producteur.'''
    
    identifiant_unique = models.CharField(max_length=500)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    numero_cni = models.CharField(max_length=200)
    identifiant_fodecc_cicc = models.CharField(max_length=200)
    numero_telephone = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    departement = models.CharField(max_length=200)
    arrondissement = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    
    

    class Meta:
        '''Meta definition for Producteur.'''

        verbose_name = 'Producteur'
        verbose_name_plural = 'Producteurs'

    def __str__(self):
        return self.nom
    
class Parcelle(models.Model):
    '''Model definition for Parcelle.'''
    numero_titre_foncier = models.CharField(max_length=200)
    statut = models.CharField(max_length=200)
    coordonnees_polygonales = models.CharField(max_length=200)
    superficie = models.FloatField()
    nombre_arbres = models.IntegerField()
    age_moyen_arbres = models.FloatField()
    producteur = models.ForeignKey(Producteur, related_name='producteur', on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for Parcelle.'''

        verbose_name = 'Parcelle'
        verbose_name_plural = 'Parcelles'

    def __str__(self):
        return self.numero_titre_foncier
    
    
    
class Cooperative(models.Model):
    '''Model definition for Cooperative.'''
    
    nom = models.CharField(max_length=200)
    image = models.ImageField(null=True)
    type_cooperative = models.CharField(max_length=200)
    siege_social = models.CharField(max_length=200)
    nom_responssable = models.CharField(max_length=200)
    contact_responssable = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    departement = models.CharField(max_length=200)
    arrondissement = models.CharField(max_length=200)
    village = models.CharField(max_length=200)
    coordonnees_gps = models.CharField(max_length=200)
    # identifiant_unique = models.CharField(max_length=500)
    # mot_pass = models.CharField(max_length=200)

    class Meta:
        '''Meta definition for Cooperative.'''

        verbose_name = 'Cooperative'
        verbose_name_plural = 'Cooperatives'

    def __str__(self):
        return self.nom
    
class Lot(models.Model):
    '''Model definition for lot.'''
    
    numero_lot = models.CharField(max_length=200)
    quantite = models.FloatField()
    type_commercial = models.CharField(max_length=200)
    taux_humidite = models.FloatField()
    date_recolt = models.DateField()
    date_livraison = models.DateField()
    cooperative = models.ForeignKey(Cooperative, related_name='lotCooperative', on_delete=models.CASCADE)
    producteur = models.ForeignKey(Producteur, related_name='lotProducteur', on_delete=models.CASCADE)
    sac = models.ForeignKey(Sac, related_name='lotSac', on_delete=models.CASCADE)
    parcelle = models.ForeignKey(Parcelle, related_name='lotParcelle', on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for lot.'''

        verbose_name = 'lot'
        verbose_name_plural = 'lots'

    def __str__(self):
        return self.numero_lot

class CooperativeProducteur(models.Model):
    '''Model definition for CooperativeProducteur.'''
    date_arriver_producteur = models.DateField()
    cooperative = models.ForeignKey(Cooperative,related_name='cooperativeProd', on_delete=models.CASCADE)
    producteur = models.ForeignKey(Producteur, related_name='producteurCoop', on_delete=models.CASCADE)

    class Meta:
        '''Meta definition for CooperativeProducteur.'''

        verbose_name = 'CooperativeProducteur'
        verbose_name_plural = 'CooperativeProducteurs'

    


