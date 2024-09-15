from django.urls import  path
from .views import BlogListview, BlogCreateview, BlogDeleteview, BlogUpdateview, BlogViewset, LoginView, RegisterView
from cocoaApp.viewsPackages.acheteurViews import AcheteurListview, AcheteurDeleteview, AcheteurCreateview, AcheteurUpdateview, AcheteurViewset
from cocoaApp.viewsPackages.SacViews import SacListview, SacDeleteview, SacCreateview, SacUpdateview, SacViewset
from cocoaApp.viewsPackages.producteurViews import ProducteurListview, ProducteurDeleteview, ProducteurCreateview, ProducteurUpdateview, ProducteurViewset
from cocoaApp.viewsPackages.parcelleViews import ParcelleListview, ParcelleDeleteview, ParcelleCreateview, ParcelleUpdateview, ParcelleViewset
from cocoaApp.viewsPackages.cooperativeViews import CooperativeListview, CooperativeDeleteview, CooperativeCreateview, CooperativeUpdateview, CooperativeViewset, loginCooperative
from rest_framework.routers import DefaultRouter




# ===========| blo urgls |========================
router = DefaultRouter()
router.register('rest',BlogViewset, basename='viewset')
AcheteurRouteur = DefaultRouter()
AcheteurRouteur.register('acheteur_rest', AcheteurViewset, basename='acheteur_viewset' )
urlpatterns = [
    path('',BlogListview.as_view(),name='List'),
    path('new/',BlogCreateview.as_view(),name='newpost'),
    path('delete/<pk>/',BlogDeleteview.as_view(),name='delete'),
    path('update/<pk>/', BlogUpdateview.as_view(), name= 'update'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/register/', RegisterView.as_view(), name='register'),
    
] + router.urls + AcheteurRouteur.urls

# ===========| acheteur urls |========================
acheteur_urls = [
    path('acheteur/',AcheteurListview.as_view(),name='List_acheteur'),
    path('new_acheteur/',AcheteurCreateview.as_view(),name='newpost_acheteur'),
    path('delete_acheteur/<pk>/',AcheteurDeleteview.as_view(),name='delete_acheteur'),
    path('update_acheteur/<pk>/', AcheteurUpdateview.as_view(), name= 'update_acheteur'),
]
urlpatterns += acheteur_urls


# ===========| sac urls |========================
sacRouteur = DefaultRouter()
sacRouteur.register('sac_rest', SacViewset, basename='sac_viewset' )
sac_urls = [
    path('sac/',SacListview.as_view(),name='List_sac'),
    path('new_sac/',SacCreateview.as_view(),name='newpost_sac'),
    path('delete_sac/<pk>/',SacDeleteview.as_view(),name='delete_sac'),
    path('update_sac/<pk>/', SacUpdateview.as_view(), name= 'update_sac'),
]
urlpatterns += sac_urls + sacRouteur.urls


# ===========| producteur urls |========================
producteurRouteur = DefaultRouter()
producteurRouteur.register('producteur_rest', ProducteurViewset, basename='producteur_viewset' )
producteur_urls = [
    path('producteur/',ProducteurListview.as_view(),name='List_producteur'),
    path('new_producteur/',ProducteurCreateview.as_view(),name='newpost_producteur'),
    path('delete_producteur/<pk>/',ProducteurDeleteview.as_view(),name='delete_producteur'),
    path('update_producteur/<pk>/', ProducteurUpdateview.as_view(), name= 'update_producteur'),
]
urlpatterns += producteur_urls + producteurRouteur.urls



# ===========| parcelle urls |========================
parcelleRouteur = DefaultRouter()
parcelleRouteur.register('parcelle_rest', ParcelleViewset, basename='parcelle_viewset' )
parcelle_urls = [
    path('parcelle/',ParcelleListview.as_view(),name='List_parcelle'),
    path('new_parcelle/',ParcelleCreateview.as_view(),name='newpost_parcelle'),
    path('delete_parcelle/<pk>/',ParcelleDeleteview.as_view(),name='delete_parcelle'),
    path('update_parcelle/<pk>/', ParcelleUpdateview.as_view(), name= 'update_parcelle'),
]
urlpatterns += parcelle_urls + parcelleRouteur.urls



# ===========| cooperative urls |========================
cooperativeRouteur = DefaultRouter()
cooperativeRouteur.register('cooperative_rest', CooperativeViewset, basename='cooperative_viewset' )
cooperative_urls = [
    path('cooperative/',CooperativeListview.as_view(),name='List_cooperative'),
    path('new_cooperative/',CooperativeCreateview.as_view(),name='newpost_cooperative'),
    path('delete_cooperative/<pk>/',CooperativeDeleteview.as_view(),name='delete_cooperative'),
    path('update_cooperative/<pk>/', CooperativeUpdateview.as_view(), name= 'update_cooperative'),
    path('logincooperative/', loginCooperative, name= 'update_cooperative'),
]
urlpatterns += cooperative_urls + cooperativeRouteur.urls