from django.apps import AppConfig
from django.apps import apps

model = apps.get_model('pessoas', 'TbPessoa')

class NoticiaConfig(AppConfig):
    name = 'noticia'
