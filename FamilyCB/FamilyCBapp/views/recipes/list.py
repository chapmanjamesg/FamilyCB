import sqlite3
from django.shortcuts import render, redirect, reverse
from FamilyCBapp.models import recipe
from ..connection import Connection


def list_recipes(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                r.id,
                r.name,
                r.instruction,
                r.servings,
                r.memberId,
                r.ingredientId,
                r.commentId,
                i.id as 'ingredientId'
                c.id AS 'commentId'
                m.id as 'memberId'
            FROM FamilyCBapp_recipe r
            LEFT JOIN FamilyCBapp_comment c
            LEFT JOIN FamilyCBapp_ingredient i
            LEFT JOIN FamilyCBapp_member m
            ON r.commentId = c.commentId
            ON r.ingredientId = i.ingredientId
            ON r.memberId = m.memberId
            """)

            all_recipes = []
            dataset = db_cursor.fetchall()

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

        if request.user.is_authenticated:
            template = 'recipes/list.html'
        else:
            template = 'recipes/list_view_only.html'

        context = {
            'recipes': all_recipes
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT into FamilyCBapp_recipe
            (
                name, instruction, servings
            )
            VALUES (?, ?, ?)
            """,
            (form_data['name'], form_data['instructions'], form_data['servings']))

        return redirect(reverse('FamilyCBapp:recipe_list'))