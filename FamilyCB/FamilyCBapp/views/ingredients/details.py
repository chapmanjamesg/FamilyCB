import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Ingredient
from FamilyCBapp.models import model_factory
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
    #     """, (ingredientId,))

    #     return db_cursor.fetchone()
    return Ingredient.objects.all()

@login_required
def ingredient_details(request, ingredientId):
    if request.method == 'GET':
        ingredient = get_ingredient(ingredientId)

        template = 'ingredients/ingredient_detail.html'
        context = {
            'ingredient': ingredient
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

            return redirect(reverse('ingredients'))

        if  ("actual_method" in form_data
            and form_data["actual_mothod"] == "DELETE"
        ):
            ingredient = Ingredient.objects.get(pk=ingredientId)
            ingredient.delete()

            return redirect(reverse('ingredients'))