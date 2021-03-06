import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from FamilyCBapp.models import Member, model_factory
from .member_details import get_member
from ..connection import Connection

def get_members():
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Family)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         f.id,
    #         f.name
    #     FROM FamilyCBapp_family f
    #     """)

    #     return db_cursor.fetchall()
    return Member.objects.all()


@login_required
def member_form(request):
    if request.method == 'GET':
        families = get_families()
        template = 'members/members_form.html'
        context = {
            'all_members': members
        }

        return render(request, template, context)

@login_required
def member_edit_form(request, memberId):
    if request.method == 'GET':
        member = get_member(memberId)
        members = get_members()
        
        template = 'members/members_form.html'
        context = {
            'member': member,
            'all_members': members
        }

        return render(request, template, context)
