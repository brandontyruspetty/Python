import pickle


def display_recipe(recipe):
    print('Name: ', recipe['Name'])
    print('Cooking Time in minutes: ', recipe['Cooking_time'])
    print('Ingredients: ', ', '.join(recipe['Ingredients']))
    print('Difficulty: ', recipe['Difficulty'])


def search_ingredient(data):
    ingredients_list = data['all_ingredients']
    indexed_ingredients_list = list(enumerate(ingredients_list, 1))

    for ingredient in indexed_ingredients_list:
        print('Item', ingredient[0], ' - ', ingredient[1])

    try:
        chosen_number = int(
            input("Enter the number of your chosen ingredient: "))
        index = chosen_number - 1
        ingredient_searched = ingredients_list[index]
        ingredient_searched = ingredient_searched.lower()
    except IndexError:
        print("The number entered is not on the list.")
    except:
        print("An unexpected error occured while finding your ingredient.")
    else:
        for recipe in data['recipes_list']:
            for recipe_ingredient in recipe['Ingredients']:
                if (recipe_ingredient == ingredient_searched):
                    print('\nThe following recipe includes the searched ingredient: ')
                    print('------------------------------------------')
                    display_recipe(recipe)


file_name = input("Enter the filename where your recipes are stored: ")

try:
    recipes_file = open(file_name, 'rb')
    data = pickle.load(recipes_file)

except FileNotFoundError:
    print("File not found. Please try another filename.")
    data = {'recipes_list': [], 'all_ingredients': []}

except:
    print("An unexpected error occurred.")
    data = {'recipes_list': [], 'all_ingredients': []}

else:
    search_ingredient(data)

finally:
    recipes_file.close()
