import sqlite3
from django.shortcuts import render, redirect, reverse
from FamilyCBapp.models import Ingredient
from ..connection import Connection


def ingredient_list(request):
    if request.method == 'GET':


        all_ingredients = Ingredient.objects.all()

        if request.user.is_authenticated:
            template = 'ingredients/ingredient_list.html'
        else:
            template = 'ingredients/ingredient_list_view_only.html'

        context = {
            'ingredients': all_ingredients
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_ingredient = Ingredient(
            name = form_data['name'],
            quantity = form_data['quantity'],
            measurement = form_data['measurement']
        )


        return redirect(reverse('recipe_edit_form'))