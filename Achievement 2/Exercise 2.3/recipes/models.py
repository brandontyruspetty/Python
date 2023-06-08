from django.db import models

# Create your models here.


class Recipes(models.Model):
    recipe_id = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    ingredients = models.CharField(max_length=240)
    description = models.TextField()

    def __str__(self):
        return str(self.name)
