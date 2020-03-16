import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCB.models import Recipe
from FamilyCB.models import model_factory
from ..connection import Connection


def get_recipe(recipeId):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Recipe)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            r.id,
            r.name,
            r.instruction,
            r.servings,
            r.ingredientId,
            r.commentId,
            c.id 
            i.id 
        FROM FamilyCBapp_recipe r
        LEFT JOIN FamilyCBapp_comment c
        LEFT JOIN FamilyCBapp_ingredient i
        ON r.ingredientId = i.id
        ON r.CommentId = c.id
        WHERE r.id = ?
        """, (recipeId,))

        return db_cursor.fetchone()

@login_required
def recipe_details(request, recipeId):
    if request.method == 'GET':
        recipe = get_recipe(recipeId)

        template = 'recipes/recipe_detail.html'
        context = {
            'recipe': recipe
        }

        return render(request, template, context)