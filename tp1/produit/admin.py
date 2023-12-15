from django.contrib import admin

# Register your models here.
from .models import produit
admin.site.register(produit)

from .models import category
admin.site.register(category)

from .models import ingredient
admin.site.register(ingredient)
