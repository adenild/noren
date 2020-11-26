from django.urls import path
from . import views, api

urlpatterns = [
    path("load/", api.load_wallets),
    path("inflows/", views.inflows),
    path("inflows/load/", api.load_operations),
]
