from django.db import models
from datetime import datetime

# Create your models here.
class ingredient(models.Model):
    ID_ing= models.AutoField(primary_key=True)
    Ing_Name= models.CharField(max_length=50)

class category(models.Model):
    ID_Cat= models.AutoField(primary_key=True)
    Cat_Name= models.CharField(max_length=50)
    
class produit(models.Model):
    ID_prd= models.AutoField(primary_key=True)
    Prd_Name= models.CharField(max_length=50)
    Price= models.FloatField(max_length=10)
    created_at = models.DateTimeField(auto_now=True)
    cat=models.ForeignKey(category, on_delete=models.CASCADE)
    ingds=models.ManyToManyField(ingredient,related_name="produits")
    def __str__(self):        
        return str(self.Prd_Name)


class Commande(models.Model):
    Description_cmd = models.CharField(max_length=50)
    Date_cmd = models.DateTimeField(default=datetime.now)
    Produit_cmd = models.ForeignKey(produit, on_delete=models.CASCADE)
    def __str__(self):        
        return str(self.Description_cmd)
