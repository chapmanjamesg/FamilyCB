import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from FamilyCB.models import Member, Family
from FamilyCB.models import model_factory
from ..connection import Connection


def get_member(memberId):
    # with sqlite3.connect(Connection.db_path) as conn:
    #     conn.row_factory = model_factory(Member)
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #     SELECT
    #         m.id,
    #         m.firstName,
    #         m.lastName,
    #         m.email,
    #     FROM FamilyCBapp_member m
    #     WHERE m.id = ?
    #     """, (memberId,))

    #     return db_cursor.fetchone()
    return Member.objects.get(pk=memberId)

@login_required
def member_details(request, memberId):
    if request.method == 'GET':
        member = get_member(memberId)

        template = 'members/member_detail.html'
        context = {
            'member': member
        }

        return render(request, template, context)