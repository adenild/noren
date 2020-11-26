from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, blank=False, null=True, unique=True, related_name="details", on_delete=models.CASCADE)
    money = models.FloatField(verbose_name="Saldo", blank=False, null=False)
