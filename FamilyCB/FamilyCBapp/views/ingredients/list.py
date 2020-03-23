import sqlite3
from django.shortcuts import render, redirect, reverse
from FamilyCBapp.models import Ingredient
from ..connection import Connection


def ingredient(request):
    if request.method == 'GET':
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     SELECT
        #         i.id,
        #         i.name,
        #         i.instruction,
        #         i.quantity
        #         i.measurement
        #     FROM FamilyCBapp_ingredient i
        #     """)

        #     all_ingredients = []
        #     dataset = db_cursor.fetchall()

            # # creates a list of all unique department objects
            # for row in dataset:
            #     department = Department()
            #     department.id = row['id']
            #     department.name = row['name']
            #     department.budget = row['budget']
            #     if(department not in all_departments):
            #         all_departments.append(department)

            # # creates a dictionary of all unique department names with values representing employee count
            # department_sizes = dict()
            # for row in dataset:
            #     if(row['name'] not in department_sizes):
            #         name = row['name']
            #         department_sizes[name] = 0

            # # and here we set the employee count for each department
            # for row in dataset:
            #     if(row['employee_id'] is not None):
            #         name = row['name']
            #         department_sizes[name] += 1

            # # transfer the department sizes to the department objects in all_departments
            # for department in all_departments:
            #     department.size = department_sizes[department.name]

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

        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT into FamilyCBapp_ingredient
        #     (
        #         name, quantity, measurement
        #     )
        #     VALUES (?, ?, ?)
        #     """,
        #     (form_data['name'], form_data['quantity'], form_data['measurement']))

        return redirect(reverse('FamilyCBapp:ingredient_list'))