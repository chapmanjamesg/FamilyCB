import sqlite3
from django.shortcuts import render, redirect, reverse
from FamilyCBapp.models import Recipe, Member, Ingredient
from ..connection import Connection

def my_recipe(request):
    if request.method == 'GET':
        # member = Member.objects.get(id=request.user.member.id)
        my_recipe = Recipe.objects.filter(member_id=request.user.member.id)


        if request.user.is_authenticated:
            template = 'recipes/my_recipe.html'
        else:
            template = 'recipes/recipe_list_view_only.html'

        context = {
            'recipes': my_recipe
        }

        return render(request, template, context)


def recipe_list(request,):
    if request.method == 'GET':
    
        all_recipes = Recipe.objects.all()
        # ingredients = Ingredient.objects.all()
        # recipe_ingredient = Ingredient.objects.filter()


        if request.user.is_authenticated:
            template = 'recipes/recipe_list.html'
        else:
            template = 'recipes/recipe_list_view_only.html'

        context = {
            'recipes': all_recipes
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        new_recipe = Recipe(
            name = form_data['name'],
            instruction = form_data['instruction'],
            servings = form_data['servings'],
            ingredient = form_data['ingredient'],
            member_id = request.user.member.id
        )
        new_recipe.save()

        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

            # db_cursor.execute("""
            # INSERT into FamilyCBapp_recipe
            # (
            #     name, instruction, servings
            # )
            # VALUES (?, ?, ?)
            # """,
            # (form_data['name'], form_data['instructions'], form_data['servings']))

        return redirect(reverse('my_recipe'))