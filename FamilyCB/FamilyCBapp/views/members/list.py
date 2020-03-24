import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from FamilyCBapp.models import Member
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def member_list(request):
    if request.method == 'GET':
    #     with sqlite3.connect(Connection.db_path) as conn:
    #         conn.row_factory = sqlite3.Row
    #         db_cursor = conn.cursor()

    #         db_cursor.execute("""
    #         select
    #             m.id,
    #             m.userId,
    #             u.firstName,
    #             u.lastName,
    #             u.email,
    #             u.userName
    #         from FamilyCBapp_member m 
    #         join auth_user u on m.userId = u.id
    #         """)

    #         all_members = []
    #         dataset = db_cursor.fetchall()

    #         for row in dataset:
    #             mem = Member()
    #             mem.id = row["id"]
    #             mem.userId = row["userId"]
    #             mem.firstName = row["firstName"]
    #             mem.lastName = row["lastName"]
    #             mem.email = row["email"]
    #             mem.userName = row["userName"]

    #             all_members.append(mem)

        all_members = Member.objects.all()

        userName = request.GET.get('userName', None)

        if userName is not None:
            all_members = all_members.filter(member_contains=userName)

        template_name = 'members/members_list.html'

        context = {
            'all_members': all_members
        }

        return render(request, template_name, context)
    
    elif request.method == 'POST':
        current_user = request.user
        current_member_user = Member.objects.get(user_id=current_user)
        form_data = request.POST

        new_member= Member(
            firstName = form_data['firstName'],
            lastName = form_data["lastName"],
            email = form_data['email'],
            userName = form_data['userName']
        )   
        new_member.save()
        # with sqlite3.connect(Connection.db_path) as conn:
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     INSERT into FamilyCB_user
        #     (
        #         name,
        #         userId,
        #     )
        #     Values (?,?)
        #     """,
        #     (form_data['name'], current_user.id))
        return redirect(reverse('home'))