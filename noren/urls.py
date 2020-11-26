from django.contrib import admin
from django.urls import path, include
from noren import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('admin/', admin.site.urls),
    path('wallet/', include('noren_wallet.urls')),
]
