from django.contrib import admin
from noren_wallet.models import Wallet, Operation

# Register your models here.

admin.site.register(Wallet)
admin.site.register(Operation)
