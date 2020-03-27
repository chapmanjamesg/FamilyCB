import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def recipe_delete(request, recipeId):
    if request.method == 'GET':
        template = 'recipes/recipe_delete.html'
        context = {'recipeId': recipeId}

        return render(request, template, context)