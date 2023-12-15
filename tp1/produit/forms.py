from django.db.models import fields   
from django import forms  
from .models import Commande   

class CommandeForm(forms.ModelForm):      
    class Meta:         
        model = Commande          
        fields="__all__" #exclude = ['Description_cmd'] #pour exclure un champ du formulaire
