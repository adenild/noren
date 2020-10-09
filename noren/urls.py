from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('noren_wallet.urls')),
    path('admin/', admin.site.urls),
]
