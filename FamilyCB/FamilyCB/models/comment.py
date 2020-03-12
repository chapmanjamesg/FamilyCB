from django.db import models


class Comment(models.Model):

    memberId = models.ForeignKey("Member", verbose_name=_("Members"), on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)