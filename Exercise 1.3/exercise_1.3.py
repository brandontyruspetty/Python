recipes_list = []
ingredients_list = []

n = int(input("How many recipes would you like to enter?: "))


def take_recipe():
    name = str(input("Enter recipe name: "))
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input(
        "Enter ingredients (separated by a comma): ").split(", ")
    recipe = {
        'name': name,
        'cooking_time': cooking_time,
        'ingredients': ingredients,
    }
    return recipe


for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Easy'
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Medium'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = 'Intermediate'
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = 'Hard'


for recipe in recipes_list:
    print('=====================================')
    print('Recipe:', recipe['name'])
    print('Cooking Time in (min):', recipe['cooking_time'])
    print('Ingredients:')
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print('Difficulty Level:', recipe['difficulty'])


def print_ingredients():
    ingredients_list.sort()
    print('Ingredients available across all recipes')
    print('=======================================================')
    for ingredient in ingredients_list:
        print(ingredient)


print_ingredients()
