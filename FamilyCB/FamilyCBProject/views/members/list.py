import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from FamilyCB.models import Member
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def list_members(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                m.id,
                m.userId,
                u.firstName,
                u.lastName,
                u.email,
                u.userName
            from FamilyCB_member m 
            join auth_user u on m.userId = u.id
            """)

            all_members = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                mem = Member()
                mem.id = row["id"]
                mem.userId = row["userId"]
                mem.firstName = row["firstName"]
                mem.lastName = row["lastName"]
                mem.email = row["email"]
                mem.userName = row["userName"]

                all_members.append(mem)

        template_name = 'members/list.html'

        context = {
            'all_members': all_members
        }

        return render(request, template_name, context)
    
    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            # db_cursor.execute("""
            # # INSERT into FamilyCB_user
            # # (

            # # )
            # # )