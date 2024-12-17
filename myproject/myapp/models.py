from django.db import models


class SingleRoll(models.Model):
    name = models.CharField(max_length=3)
