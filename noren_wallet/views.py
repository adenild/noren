from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    print(f"Usuário: {request.user}, ID: {request.user.id}")
    return render(request, "wallet/homepage.html", {'base': 'base.html'})

