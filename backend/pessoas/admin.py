from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models.pessoa import Pessoa
from .models.fone import Fone
from .models.user import CustomUser

admin.site.register(CustomUser, UserAdmin)

class Pessoas(admin.ModelAdmin):
    list_display = ('pessoa_id','cpf_pessoa', 'nome_pessoa', 'username')
    list_display_links = ('cpf_pessoa', 'nome_pessoa')
    search_fields = ('cpf_pessoa', 'nome_pessoa')
    list_per_page = 10

admin.site.register(Pessoa, Pessoas)

class Fones(admin.ModelAdmin):
    list_display = ('fone_id', 'nr_fone',)
    list_display_links = ('fone_id','nr_fone',)
    search_fields = ('nr_fone', )
    list_per_page = 10

admin.site.register(Fone, Fones)
