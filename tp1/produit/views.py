from django.shortcuts import render,redirect
from .models import produit
from .forms import CommandeForm
from .models import Commande
# Create your views here.

def afficher_produits(request):
    produits = produit.objects.all()
    return render(request,"index.html",{"produits":produits})

def rechercher_produits(request):
    once=False
    found=True    
    if request.method == "GET":          
        query=request.GET.get('search')          
        if query:         
            produits=produit.objects.filter(Prd_Name__contains=query) 
            once=True
            if not produits:
                found=False
                produits = produit.objects.filter(ingds__Ing_Name__contains=query).distinct             
            return render(request,'search.html', {'produits': produits,'once':once,'found':found})          
        return render(request,'search.html')
    
def commander_prd(request):     
    if request.method == 'POST':         
        form = CommandeForm(request.POST)                   
        if form.is_valid():             
            form.save()             
            form = CommandeForm()             
            mssg="commande envoyée, vous pouvez saisir une autre"             
            # return redirect("listing")  #redirection vers la page de l’url: listing   
            Commandes = Commande.objects.all() 
            return render(request,"Commandeliste.html",{"Commandes":Commandes})      
    else:         
        form = CommandeForm()   #créer une instance de formulaire vierge         
        mssg ="veuillez remplir tous les champs!"         
        return render(request,"commande.html",{"form":form,"message":mssg})      

def afficher_Commandes(request):
    if request.method == "GET":          
        query=request.GET.get('ajouter') 
    return render(request,'commande.html')

def afficher_cmd(request):
    cmds=Commande.objects.all()
    return render(request,"CmdList.html",{"commandes":cmds})

def edit_cmd(request, pk):
    cmd=Commande.objects.get(id=pk) # récupérer l'instance de "commande" correspondante
    if request.method=='POST':
        form =CommandeForm(request.POST, instance=cmd)
         #create new order (commande) instance from post data. This instance will replace an existing one in the database (the cmd instance).
        if form.is_valid():
            form.save()
            return redirect("CmdList") #rediriger vers l’url: CmdList.
    else:
        form=CommandeForm(instance=cmd) #fournir une instance pré-remplie de formulaire 
        return render(request,'CmdEdit.html',{"form":form})
    

def delete_cmd(request, pk):
    cmd = Commande.objects.get(id=pk)
    if request.method == 'POST':
        cmd.delete()
        return redirect("CmdList")  # Rediriger vers la liste des commandes après suppression.
    return render(request, 'confirm_delete.html', {'cmd': cmd})
