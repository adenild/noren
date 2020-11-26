from django.conf import settings
from django.db import models


# Create your models here.
class Wallet(models.Model):
    title = models.CharField(verbose_name="Título", null=False, blank=False, max_length=100)
    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    money = models.FloatField(verbose_name="Saldo", null=False, blank=False)
    owner = models.OneToOneField(verbose_name="Proprietário", null=False, blank=False, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateField(verbose_name="Data de Criação", auto_now_add=True)


class Operation(models.Model):
    title = models.CharField(verbose_name="Título", null=False, blank=False, max_length=100)
    operation = models.CharField(verbose_name="Operação", null=False, blank=False, max_length=2)

    description = models.TextField(verbose_name="Descrição", null=True, blank=True)
    date = models.DateField(verbose_name="Data", null=False, blank=False)
    value = models.FloatField(verbose_name="Valor", null=False, blank=False)

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
