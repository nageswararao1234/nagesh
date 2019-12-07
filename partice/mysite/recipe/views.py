# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render
from django .http import HttpResponse, HttpResponseRedirect



def home(request):
    recipes = Recipe.objects.order_by('-id')
    return render(request, "home.html", {"recipes":recipes})



def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/recipe/")
        else:
            return render(request, "create.html", {"form":form.errors})


    else:
        form = RecipeForm()
        return render(request, "create.html", {"form":form})





