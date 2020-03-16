import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Member, Family, model_factory
from .details import get_member
from ..connection import Connection

def get_families():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Family)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            f.id,
            f.name
        FROM FamilyCBapp_family d
        """)

        return db_cursor.fetchall()


@login_required
def member_form(request):
    if request.method == 'GET':
        families = get_families()
        template = 'members/members_form.html'
        context = {
            'all_families': families
        }

        return render(request, template, context)

@login_required
def member_edit_form(request, memberId):
    if request.method == 'GET':
        member = get_member(memberId)
        families = get_families()
        
        template = 'members/members_form.html'
        context = {
            'member': member,
            'all_families': families
        }

        return render(request, template, context)
