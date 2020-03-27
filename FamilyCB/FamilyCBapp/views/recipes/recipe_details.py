import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Recipe, Ingredient
from FamilyCBapp.models import model_factory
from ..connection import Connection


def get_recipe(recipeId):

    return Recipe.objects.get(pk=recipeId)

@login_required
def recipe_details(request, recipeId):
    if request.method == 'GET':
        recipe = get_recipe(recipeId)
        # recipe_ingredients = Ingredient.objects.filter(recipe_id=recipeId)

        template = 'recipes/recipe_detail.html'
        context = {
            'recipe': recipe
            # 'ingredient': recipe_ingredients
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            # retrieve it first
            recipe_to_update = Recipe.objects.get(pk=recipeId)

            # reassign a property's value
            recipe_to_update.name = form_data['name']
            recipe_to_update.instruction = form_data['instruction']
            recipe_to_update.servings = form_data['servings']
            recipe_to_update.ingredient = form_data['ingredient']
            # recipe_to_update.commentId = form_data['commentId']

            # save the change to the db
            recipe_to_update.save()

            return redirect(reverse('home'))

        elif  ("actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            recipe = Recipe.objects.get(pk=recipeId)
            print('test', recipe)
            recipe.delete()

            return redirect(reverse('home'))

