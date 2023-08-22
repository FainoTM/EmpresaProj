from django.contrib import admin
from core.models import Cargo, Funcionario, Servico


@admin.register(Cargo)
class CargoAdimin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo', 'foto')
    list_editable = ('ativo', )

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('tipo',)