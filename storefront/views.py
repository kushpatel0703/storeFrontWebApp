from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import inventory

def index(request):
    inventoryPt1 = inventory.objects.all()[:3]
    inventoryPt2 = inventory.objects.all()[3:6]
    template = loader.get_template('storefront/index.html')
    context = { 'inventoryPt1' : inventoryPt1, 'inventoryPt2' : inventoryPt2,}
    return HttpResponse(template.render(context, request))
