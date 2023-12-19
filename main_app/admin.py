from django.contrib import admin
# add Feeding to the import
from .models import Frog, Feeding

admin.site.register(Frog)
# register the new Feeding Model 
admin.site.register(Feeding)

