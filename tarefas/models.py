from django.db import models
from django.utils import timezone
# Create your models here.

class Tarefa(models.Model):
    
    class Prioridade(models.IntegerChoices):
        BAIXA = 1, 'Baixa'
        MEDIA = 2, 'Média'
        ALTA  = 3, 'Alta'
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    criation_date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(
        choices=Prioridade.choices,
        default=Prioridade.BAIXA,
    )
    
    