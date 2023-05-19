import pickle


def calc_difficulty(recipe):

    if recipe['Cooking_Time'] < 10 and len(recipe['Ingredients']) < 4:
        difficulty = 'Easy'

    elif recipe['Cooking_Time'] < 10 and len(recipe['Ingredients']) >= 4:
        difficulty = 'Medium'

    elif recipe['Cooking_Time'] >= 10 and len(recipe['Ingredients']) < 4:
        difficulty = 'Intermediate'

    elif recipe['Cooking_Time'] >= 10 and len(recipe['Ingredients']) >= 4:
        difficulty = 'Hard'

    return difficulty


def take_recipe():
    name = input("Enter name of recipe: ")
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = input(
        "Enter ingredients (separated by a comma): ").split(", ")
    recipe = {
        'Name': name,
        'Cooking_Time': cooking_time,
        'Ingredients': ingredients,
    }
    recipe['Difficulty'] = calc_difficulty(recipe)
    return recipe


recipes_list = []
all_ingredients = []

file_name = input("Enter a filename for your recipes: ")

try:
    recipes_file = open(file_name, 'rb')
    data = pickle.load(recipes_file)
except FileNotFoundError:
    print("File not found. Creating new file.")
    data = {
        'recipes_list': [],
        'all_ingredients': [],
    }
except:
    print("An unexpected error occurred. Creating new file.")
    data = {
        'recipes_list': [],
        'all_ingredients': [],
    }
else:
    recipes_file.close()
finally:
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']

num_of_recipes = int(input("How many recipes would you like to enter?: "))

for i in range(num_of_recipes):
    recipe = take_recipe()
    print(recipe)

    for ingredient in recipe['Ingredients']:
        if not ingredient in all_ingredients:
            all_ingredients.append(ingredient)

    recipes_list.append(recipe)

data = {'recipes_list': recipes_list, 'all_ingredients': all_ingredients}

new_filename = input("Enter your new filename.")
with open(new_filename, 'wb') as file:
    pickle.dump(data, file)
