from django.db import models



class Family(models.Model):

    name = models.models.CharField(max_length=50)
    creator = models.ForeignKey("User", on_delete=models.CASCADE)
    memberId = models.ManyToManyField("User", on_delete=models.CASCADE)
    recipeId = models.ManyToManyField("Recipe", on_delete=models.CASCADE)
    privacy = models.BooleanField()




