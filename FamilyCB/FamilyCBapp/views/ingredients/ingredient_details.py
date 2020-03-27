import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Ingredient
from FamilyCBapp.models import Recipe
from FamilyCBapp.models import model_factory
from ..connection import Connection


def get_ingredient(ingredientId):

    return Ingredient.objects.get(pk=ingredientId)


@login_required
def ingredient_details(request, ingredientId, recipeId):
    if request.method == 'GET':

        ingredient = get_ingredient(ingredientId)

        template = 'ingredients/ingredient_detail.html'
        context = {
            'ingredient': recipe_ingredient
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_mothod"] == "PUT"
        ):
            # retrieve it first
            ingredient_to_update = Ingredient.objects.get(pk=ingredientId)

            # reassign a property's value
            ingredient_to_update.name = form_data['name']
            ingredient_to_update.quantity = form_data['quantity']
            ingredient_to_update.measurement = form_data['measurement']

            # save the change to the db
            ingredient_to_update.save()

            return redirect(reverse('ingredient_list'))

        if  ("actual_method" in form_data
            and form_data["actual_mothod"] == "DELETE"
        ):
            ingredient = Ingredient.objects.get(pk=ingredientId)
            ingredient.delete()

            return redirect(reverse('ingredient_list'))