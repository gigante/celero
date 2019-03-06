import uuid
from django.db import models


class FlowType:
    RECIPE = 'REC'
    EXPENSE = 'EXP'

    TYPES = (
        (RECIPE, 'Receita'),
        (EXPENSE, 'Despesa'),
    )


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(verbose_name='nome', max_length=60)
    currency = models.DecimalField(verbose_name='valor', max_digits=10, decimal_places=2)
    flow = models.CharField(
        'tipo', max_length=3, choices=FlowType.TYPES,
        default=FlowType.RECIPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        signal = "+" if self.flow == FlowType.RECIPE else "-"
        return f'{self.name}: {signal} R$ {self.currency}'
