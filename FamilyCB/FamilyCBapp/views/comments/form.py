import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Comment, model_factory
from .details import get_comment
from ..connection import Connection

def get_comments():
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Comment)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         c.id,
    #         c.comment,
    #         c.memberId,
    #         r.commentId

    #     FROM FamilyCBapp_comment c
    #     LEFT JOIN FamilyCBapp_comment r
    #     ON  c.id = r.commentId
    #     WHERE c.id = ?
    #     """)

    #     return db_cursor.fetchall()
    return Comment.objects.all()


@login_required
def comment_form(request):
    if request.method == 'GET':
        comments = get_comment()
        template = 'comments/comments_form.html'
        context = {
            'all_comments': comments
        }

        return render(request, template, context)

@login_required
def comment_edit_form(request, commentId):
    if request.method == 'GET':
        comment = get_comment(commentId)
        comments = get_comments()
        
        template = 'comments/comments_form.html'
        context = {
            'comment': comment,
            'all_comments': comments
        }

        return render(request, template, context)
