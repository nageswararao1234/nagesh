# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=150)
    ingredients = models.CharField(max_length=200)
    process = models.TextField()



    def __str__(self):
        return self.name
