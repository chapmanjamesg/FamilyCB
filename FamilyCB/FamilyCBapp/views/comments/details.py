import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCB.models import Comment
from FamilyCB.models import model_factory
from ..connection import Connection


def get_comment(commentId):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Comment)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.comment,
            c.memberId,
            r.commentId

        FROM FamilyCBapp_comment c
        LEFT JOIN FamilyCBapp_recipe r
        ON  c.id = r.commentId
        WHERE c.id = ?
        """, (commentId,))

        return db_cursor.fetchone()

@login_required
def comment_details(request, commentId):
    if request.method == 'GET':
        comment = get_comment(commentId)

        template = 'comments/comment_detail.html'
        context = {
            'comment': comment
        }

        return render(request, template, context)