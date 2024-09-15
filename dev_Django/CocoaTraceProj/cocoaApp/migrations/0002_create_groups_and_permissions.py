# migrations/0002_create_groups_and_permissions.py
from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth.Group')
    Permission = apps.get_model('auth.Permission')

    # Créer des groupes
    admin_group, created = Group.objects.get_or_create(name='Admin')
    adminCoop_group, created = Group.objects.get_or_create(name='AdminCoop')
    acteur_group, created = Group.objects.get_or_create(name='Acteur')

    # Créer des permissions personnalisées
    can_publish, created = Permission.objects.get_or_create(codename='gerer_parcelle', name='gerer les parcelles')
    can_approve, created = Permission.objects.get_or_create(codename='gerer_producteur', name='gerer les producteurs')
    can_approve, created = Permission.objects.get_or_create(codename='gerer_lot', name='gerer les lots')
    can_approve, created = Permission.objects.get_or_create(codename='gerer_vente', name='gerer les ventes')
    can_approve, created = Permission.objects.get_or_create(codename='gerer_cooperative', name='gerer les ventes')

    # Attribuer des permissions aux groupes
    admin_group.permissions.add(gerer_parcelle, gerer_cooperative)
    acteur_group.permissions.add(gerer_vente)
    adminCoop_group.permissions.add(gerer_parcelle, gerer_producteur, gerer_lot, gerer_vente, gerer_cooperative)

class Migration(migrations.Migration):
    dependencies = [
        ('cocoaApp', '0001_initial'),  # Remplacez par le nom de votre migration précédente
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions),
    ]