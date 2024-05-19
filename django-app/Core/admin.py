from django.contrib import admin
from Core.models import CadastroCliente


@admin.register(CadastroCliente)
class CadastroClienteAdmin(admin.ModelAdmin):
    list_display = 'nome',

# Register your models here.
