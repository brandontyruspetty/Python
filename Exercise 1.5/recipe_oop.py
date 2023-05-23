class Recipe(object):

    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def add_ingredients(self, *args):
        self.ingredients = args
        self.update_all_ingredients()

    def get_ingredients(self):
        print("\nIngredients: ")
        print("-------------")
        for ingredient in self.ingredients:
            print('-' + str(ingredient))

    def get_difficulty(self):
        difficulty = self.calc_difficulty(self.cooking_time, self.ingredients)
        output = "Difficulty: " + str(self.cooking_time)
        self.difficulty = difficulty
        return output

    def calc_difficulty(self, cooking_time, ingredients):
        if (cooking_time < 10) and (len(ingredients) < 4):
            difficulty_level = "Easy"
        elif (cooking_time < 10) and (len(ingredients) >= 4):
            difficulty_level = "Medium"
        elif (cooking_time >= 10) and (len(ingredients) < 4):
            difficulty_level = "Intermediate"
        elif (cooking_time >= 10) and (len(ingredients) >= 4):
            difficulty_level = "Hard"
        else:
            print("Something went wrong, please try again")

        return difficulty_level

    def search_ingredient(self, ingredient, ingredients):
        if ingredient in self.ingredients:
            return True
        else:
            return False

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)

    def __str__(self):
        output = "Name: " + self.name + \
            "\nCooking Time (in minutes): " + str(self.cooking_time) + \
            "\nIngredients: " + str(self.ingredients) + \
            "\nDifficulty: " + str(self.difficulty) + \
            "\n--------------------------"
        for ingredient in self.ingredients:
            output += "- " + ingredient + "\n"
            return output

    def recipe_search(self, recipes_list, ingredient):
        data = recipes_list
        search_term = ingredient
        for recipe in data:
            if self.search_ingredient(search_term, recipe.ingredients):
                print(recipe)


recipes_list = []

tea = Recipe("Tea")
tea.add_ingredients("Water", "Tea Leaves", "Sugar")
tea.set_cooking_time(5)
tea.get_difficulty()

recipes_list.append(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee powder", "Water", "Milk")
coffee.set_cooking_time(5)
coffee.get_difficulty()

recipes_list.append(coffee)

cake = Recipe("Cake")
cake.add_ingredients("Flour", "Sugar", "Eggs", "Milk",
                     "Butter", "Vanilla Essence")
cake.set_cooking_time(50)
cake.get_difficulty()

recipes_list.append(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients("Banana", "Milk", "Sugar", "Ice")
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_difficulty()

recipes_list.append(banana_smoothie)

print("--------------------------")
print("Recipes List")
print("--------------------------")
for recipe in recipes_list:
    print(recipe)

print("--------------------------")
print("Results for recipe_search with Water: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Water")

print("--------------------------")
print("Results for recipe_search with Sugar: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Sugar")

print("--------------------------")
print("Results for recipe_search with Bananas: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Bananas")
