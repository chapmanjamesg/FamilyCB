from django.db import models


class Recipe(models.Model):

   
    name = models.CharField(max_length=255)
    # ingredientId = models.ManyToManyField("Ingredient", verbose_name=("ingredients"), null=True)
    ingredient = models.CharField(max_length=1000)
    instruction = models.CharField(max_length=1000)
    # commentId = models.ManyToManyField("Comment", verbose_name=("Comments"), null=True)
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    servings = models.IntegerField()



