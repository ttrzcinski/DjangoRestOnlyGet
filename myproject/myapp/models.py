from django.db import models

# Single roll of a die
class SingleRoll(models.Model):
    name = models.CharField(max_length=3)
