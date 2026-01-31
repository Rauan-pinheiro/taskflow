from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority' ,'status', 'criation_date')
    
    list_filter = ('priority', 'status')

    search_fields = ('title',)