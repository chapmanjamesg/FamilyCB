from django.db import models
from .member import Member



class Family(models.Model):

    name = models.CharField(max_length=50)
    creator = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="creator")
    memberId = models.ManyToManyField(Member, verbose_name=("Members"))
    recipeId = models.ManyToManyField("Recipe")
    privacy = models.BooleanField()




