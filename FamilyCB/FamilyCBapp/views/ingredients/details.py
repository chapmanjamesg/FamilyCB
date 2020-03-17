import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCB.models import Ingredient
from FamilyCB.models import model_factory
from ..connection import Connection


def get_ingredient(ingredientId):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Ingredient)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            i.id,
            i.name,
            i.quantity,
            i.measurement,
            r.ingredientId

        FROM FamilyCBapp_ingredient i
        LEFT JOIN FamilyCBapp_recipe r
        ON  i.id = r.ingredientId
        WHERE i.id = ?
        """, (ingredientId,))

        return db_cursor.fetchone()

@login_required
def ingredient_details(request, ingredientId):
    if request.method == 'GET':
        ingredient = get_ingredient(ingredientId)

        template = 'ingredients/ingredient_detail.html'
        context = {
            'ingredient': ingredient
        }

        return render(request, template, context)