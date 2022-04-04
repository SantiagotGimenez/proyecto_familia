from django.contrib import admin

# Register your models here.
from .models import Familiares

class FamiliaresAdmin(admin.ModelAdmin):
    list_display = ('nombre','parentesco','edad','cumpleanios')

admin.site.register(Familiares,FamiliaresAdmin)