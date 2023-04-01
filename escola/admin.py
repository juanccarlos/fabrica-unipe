from django.contrib import admin
from escola.models import Aluno

class Alunos(admin.ModelAdmin):
    list_diplay = ('id', 'nome', 'rgm', 'data_nascimeno')
    search_fields = ('rgm',)

admin.site.register(Aluno, Alunos)