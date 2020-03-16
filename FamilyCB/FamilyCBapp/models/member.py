from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    # userName = models.CharField(max_length=50, null=True)
    # firstName = models.CharField(max_length=255, null=True)
    # lastName = models.CharField(max_length=50, null=True)
    # email = models.models.EmailField(max_length=254)
    familyId = models.ForeignKey("Family", verbose_name=("Families"), on_delete=models.CASCADE, null=True)
    



    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    
    # These receiver hooks allow you to continue to
    # work with the `User` class in your Python code.


    # Every time a `User` is created, a matching `Librarian`
    # object will be created and attached as a one-to-one
    # property
    @receiver(post_save, sender=User)
    def create_member(sender, instance, created, **kwargs):
        if created:
            Member.objects.create(user=instance)

    # Every time a `User` is saved, its matching `Librarian`
    # object will be saved.
    @receiver(post_save, sender=User)
    def save_member(sender, instance, **kwargs):
        instance.member.save