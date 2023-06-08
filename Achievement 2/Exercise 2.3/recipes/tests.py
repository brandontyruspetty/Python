from django.test import TestCase
from .models import Recipes

# Create your tests here.


class RecipesModelTest(TestCase):

    def setUpTestData():
        # set up non-modified objects used by all test methods
        Recipes.objects.create(name='tea', cooking_time=5, ingredients='Tea Leaves, Water',
                               description='Boil water.  Then put tea leaves in for 5 min.', favorite=True)

    def test_recipe_name(self):
        recipe = Recipes.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_cooking_time_max_length(self):
        recipe = Recipes.objects.get(id=1)
        max_length = recipe._meta.get_field('cooking_time').max_length
        self.assertEqual(max_length, 5)

    def test_ingredients_number(self):
        recipe = Recipes.objects.get(id=1)
        field_label = recipe._meta.get_field(
            'ingredients').verbose_ingredients
        self.assertEqual(field_label, 'ingredients')
