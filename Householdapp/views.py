from django.shortcuts import render
from django.http import HttpResponse
from .models import Refrigerator, Grocery, Unit
from .forms import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def Refrigeratorview(request):
    object_list = Refrigerator.objects.all()
    # for item in object_list:
    #     item.grocery_name = Grocery.objects.name
    return render(request, 'refrigerator.html', {'object_list': object_list})


def RefrigeratorAddview(request):
    if request.method == 'POST':
        form = RefrigeratorForm(request.POST)
        print('debug1', form)
        grocery = Grocery.objects.get(id=form.cleaned_data['grocery'])
        unit = Unit.objects.get(id=form.cleaned_data['unit'])
        refrigerator = Refrigerator(
            grocery=grocery, quantity=form.cleaned_data['quantity'], unit=unit)
        refrigerator.save()

    else:
        form = RefrigeratorForm()
    return render(request, 'refrigerator_add.html', {'form': form})


def UnitAddview(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
        print(form)
        unit = Unit(name=form.cleaned_data['unit_name'])
        unit.save()
    else:
        form = UnitForm()
    return render(request, 'unit_add.html', {'form': form})


def GroceryAddview(request):
    if request.method == 'POST':
        form = GroceryForm(request.POST)
        print(form)
        grocery = Grocery(name=form.cleaned_data['grocery_name'])
        grocery.save()
    else:
        form = GroceryForm()
    return render(request, 'grocery_add.html', {'form': form})
