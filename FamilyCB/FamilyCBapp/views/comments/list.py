import sqlite3
from django.shortcuts import render, redirect, reverse
from FamilyCBapp.models import Comment
from ..connection import Connection


def comment_list(request):
    if request.method == 'GET':
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     SELECT
        #         c.id,
        #         c.comment,
        #         c.memberId,
        #         r.commentId
        #     FROM FamilyCBapp_comment c
        #     LEFT JOIN FamilyCBapp_recipe r 
        #     ON c.id = r.commentId
        #     """)

        #     all_comments = []
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
        all_comments = Comment.objects.all()

        memberId = request.GET.get('memberId', None)
        
        if memberId is not None :
            all_comments = all_comments.filter(comment_contains=memberId)
        if request.user.is_authenticated:
            template = 'comments/comment_list.html'
        else:
            template = 'comments/comment_list_view_only.html'

        context = {
            'comments': all_comments
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        
        new_comment = Comment(
           comment = form_data['comment'],
           memberId = form_data['memberId'],
        )

        new_comment.save()
        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT into FamilyCBapp_comment
        #     (
        #         comment, memberId
        #     )
        #     VALUES (?, ?)
        #     """,
        #     (form_data['comment'], form_data['memberId']))

        return redirect(reverse('FamilyCBapp:comment_list'))