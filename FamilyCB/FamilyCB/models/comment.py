from django.db import models


class Comment(models.Model):

    userId = models.ForeignKey("User", verbose_name=_("Users"), on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)