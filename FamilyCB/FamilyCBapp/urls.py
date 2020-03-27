from django.urls import path, reverse
from django.conf.urls import include
from FamilyCBapp import views
from .views import *

app_name = 'FamilyCBapp'
urlpatterns = [
    path('', recipe_list, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),

    path('recipes/', my_recipe, name='my_recipe'),
    path('recipes/form', recipe_form, name='recipe_form'),
    path('recipes/<int:recipeId>/', recipe_details, name='recipe_details'),
    path('recipes/<int:recipeId>/form/', recipe_edit_form, name='recipe_edit_form'),
    path('recipes/delete/<int:recipeId>', recipe_delete, name='recipe_delete'),

    path('members/', member_list, name='member_list'),
    path('member/form', member_form, name='member_form'),
    path('members/<int:memberId>/', member_details, name='member_details'),
    path('members/<int:memberId>/form/', member_edit_form, name='member_edit_form'),

    path('ingredients/', ingredient_list, name='ingredient_list'),
    path('ingredients/form', ingredient_form, name='ingredient_form'),
    path('ingredients/<int:ingredientId>', ingredient_details, name='ingredient_details'),
    path('ingredients/<int:ingredientId>/form/', ingredient_edit_form, name='ingredient_edit_form'),

    path('comments/', comment_list, name='comment_list'),
    path('comments/form', comment_form, name='comment_form'),
    path('comments/<int:commentId>', comment_details, name='comment_details'),
    path('comments/<int:commentId/form/>', comment_edit_form, name='comment_edit_form')
]
