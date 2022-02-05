from django.db import models


class ChemProblems(models.Model):
    problem = models.CharField(max_length=128)
