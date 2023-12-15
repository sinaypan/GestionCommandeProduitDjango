from django.urls import path
from . import views



urlpatterns = [
    path('list_produits/',views.afficher_produits),
    path('recherche_produits/',views.rechercher_produits, name="listing"),
    path('commander/',views.commander_prd, name="cmd"),
    path('commandes/',views.afficher_cmd, name="CmdList"),
    path('commandes/edit/<int:pk>/', views.edit_cmd, name='CmdEdit'),
    path('commandes/delete/<int:pk>/', views.delete_cmd, name='CmdDelete'),
]