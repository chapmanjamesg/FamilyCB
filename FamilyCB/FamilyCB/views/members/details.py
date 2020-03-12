import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCB.models import User, Family
from FamilyCB.models import model_factory
from ..connection import Connection


def get_User(userId):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(User)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.firstName,
            u.lastName,
            u.email,
            u.familyId
        FROM FamilyCB_User u
        WHERE u.id = ?
        """, (userId,))

        return db_cursor.fetchone()

@login_required
def user_details(request, userId):
    if request.method == 'GET':
        librarian = get_User(userId)

        template = 'users/detail.html'
        context = {
            'user': user
        }

        return render(request, template, context)