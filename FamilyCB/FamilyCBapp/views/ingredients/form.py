import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Ingredient, model_factory
# from .details import get_member
from .details import get_ingredient
from ..connection import Connection

def get_ingredients():
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Ingredient)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         i.id,
    #         i.name,
    #         i.quantity,
    #         i.measurement,
    #         r.ingredientId

    #     FROM FamilyCBapp_ingredient i
    #     LEFT JOIN FamilyCBapp_ingredient r
    #     ON  i.id = r.ingredientId
    #     WHERE i.id = ?
    #     """)

    #     return db_cursor.fetchall()
    return Ingredient.objects.all()


@login_required
def ingredient_form(request):
    if request.method == 'GET':
        ingredients = get_ingredient()
        template = 'ingredients/ingredients_form.html'
        context = {
            'all_ingredients': ingredients
        }

        return render(request, template, context)

@login_required
def ingredient_edit_form(request, ingredientId):
    if request.method == 'GET':
        ingredient = get_ingredient(ingredientId)
        ingredients = get_ingredients()
        
        template = 'ingredients/ingredients_form.html'
        context = {
            'ingredient': ingredient,
            'all_ingredients': ingredients
        }

        return render(request, template, context)
