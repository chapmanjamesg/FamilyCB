import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Recipe
from FamilyCBapp.models import model_factory
from ..connection import Connection


def get_recipe(recipeId):
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Recipe)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         r.id,
    #         r.name,
    #         r.instruction,
    #         r.servings,
    #         r.ingredientId,
    #         r.commentId,
    #         c.id 
    #         i.id 
    #     FROM FamilyCBapp_recipe r
    #     LEFT JOIN FamilyCBapp_comment c
    #     LEFT JOIN FamilyCBapp_ingredient i
    #     ON r.ingredientId = i.id
    #     ON r.CommentId = c.id
    #     WHERE r.id = ?
    #     """, (recipeId,))

    #     return db_cursor.fetchone()
    return Recipe.objects.get(pk=recipeId)

@login_required
def recipe_details(request, recipeId):
    if request.method == 'GET':
        recipe = get_recipe(recipeId)

        template = 'recipes/recipe_detail.html'
        context = {
            'recipe': recipe
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_mothod"] == "PUT"
        ):
            # retrieve it first
            recipe_to_update = Recipe.objects.get(pk=recipeId)

            # reassign a property's value
            recipe_to_update.name = form_data['name']
            recipe_to_update.instruction = form_data['instruction']
            recipe_to_update.servings = form_data['servings']
            recipe_to_update.ingredientId = form_data['ingredientId']
            recipe_to_update.commentId = form_data['commentId']

            # save the change to the db
            recipe_to_update.save()

            return redirect(reverse('recipes'))

        if  ("actual_method" in form_data
            and form_data["actual_mothod"] == "DELETE"
        ):
            recipe = Recipe.objects.get(pk=recipeId)
            recipe.delete()

            return redirect(reverse('recipes'))

