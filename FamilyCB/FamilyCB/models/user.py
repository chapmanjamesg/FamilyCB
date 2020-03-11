from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField()
    firstName = models.CharField(max_length=255, null=True)
    lastName = models.CharField(max_length=50, null=True)
    email = models.models.EmailField(max_length=254)
    familyId = models.ForeignKey("Family", verbose_name=_("Families"), on_delete=models.CASCADE)
    



    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'