from django.core import serializers
from django.http import HttpResponse, JsonResponse

from noren_wallet.models import Operation, Wallet


def load_operations(request):
    data = Operation.objects.filter(id=request.user.id).filter(operation=request.POST["operation"])
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')


def load_wallets(request):
    data = Wallet.objects.filter(id=request.user.id).order_by('pk')
    data = serializers.serialize('json', data)
    return HttpResponse(data, content_type='application/json')
