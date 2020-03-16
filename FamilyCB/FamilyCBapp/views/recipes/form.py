import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Recipe, model_factory
from .details import get_member
from .details import get_recipe
from ..connection import Connection

def get_recipes():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Recipe)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            r.id,
            r.name,
            r.instruction,
            r.servings,
            r.ingredientId
            r.commentId
            c.id
            i.id
        FROM FamilyCBapp_recipe r
        LEFT JOIN FamilyCBapp_comment c
        LEFT JOIN FamilyCBapp_ingredient i
        ON r.ingredientId = i.id
        ON r.commentId = c.id
        """)

        return db_cursor.fetchall()


@login_required
def recipe_form(request):
    if request.method == 'GET':
        recipes = get_recipe()
        template = 'recipes/recipes_form.html'
        context = {
            'all_recipes': recipes
        }

        return render(request, template, context)

@login_required
def recipe_edit_form(request, recipeId):
    if request.method == 'GET':
        recipe = get_recipe(recipeId)
        recipes = get_recipes()
        
        template = 'recipes/recipes_form.html'
        context = {
            'recipe': recipe,
            'all_recipes': recipes
        }

        return render(request, template, context)
