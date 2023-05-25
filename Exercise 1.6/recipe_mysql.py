# importing connector module
import mysql.connector

# intializing connection object with user parameters
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password'
)

# initializing cursor object
cursor = conn.cursor()

# creating database
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# allowing script to access database
cursor.execute("USE task_database")

# creating Recipe table with specific columns
cursor.execute('''CREATE TABLE IF NOT EXISTS Recipes(
id INT PRIMARY KEY AUTO_INCREMENT, 
name VARCHAR(50), 
ingredients VARCHAR(255), 
cooking_time INT, 
difficulty VARCHAR(20) 
)''')

# loop running main menu, continues to loop as long as user doesn't choose 'quit'


def main_menu(conn, cursor):
    choice = ""
    while (choice != 'quit'):
        print("\n==================================")
        print("\nMain Menu:")
        print("===================")
        print("What would you like to do? Pick a number:")
        print(" 1. Create a recipe")
        print(" 2. Search for a recipe")
        print(" 3. Update a recipe")
        print(" 4. Delete a recipe")
        print(" 5. View all recipes")
        print("\n Type 'quit' to exit the program.")
        choice = input("\nYour choice: ")
        print("\n==================")

        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            view_all_recipes(conn, cursor)


# creating main menu options
def create_recipe(conn, cursor):
    recipe_ingredients = []
    name = str(input("\nEnter name of the recipe: "))
    cooking_time = int(input("Enter cooking time of recipe (in minutes): "))
    ingredient = str(input("Enter ingredients: "))
    recipe_ingredients.append(ingredient)
    difficulty = calculate_difficulty(cooking_time, recipe_ingredients)
    recipe_ingredients_str = ", ".join(recipe_ingredients)
    sql = 'INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)'
    val = (name, recipe_ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("Recipe saved to database.")


def calculate_difficulty(cooking_time, recipe_ingredients):
    if (cooking_time < 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Easy"
    elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Medium"
    elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty_level = "Intermediate"
    elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty_level = "Hard"
    else:
        print("Unexpected error occurred, please try again")

    print("Difficulty level: ", difficulty_level)
    return difficulty_level


def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute('SELECT ingredients FROM Recipes')
    results = cursor.fetchall()
    # iterates through the results list for each recipe tuple
    for recipe_ingredients_list in results:
        # iterates through recipe ingredients tuple
        for recipe_ingredients in recipe_ingredients_list:
            # split each recipe ingredients tuple
            recipe_ingredient_split = recipe_ingredients.split(", ")
            all_ingredients.extend(recipe_ingredient_split)

    # remove duplicates from the list
    all_ingredients = list(dict.fromkeys(all_ingredients))

    # shows user all ingredients and adds enumeration to each one
    all_ingredients_list = list(enumerate(all_ingredients))

    print("\nAll ingredients list:")
    print("-------------------------")

    for index, tup in enumerate(all_ingredients_list):
        print(str(tup[0]+1) + ". " + tup[1])

    try:
        # User input to pick number from all_ingredients_list
        ingredient_searched_num = input(
            "\nEnter number corresponding to ingredient you are searching for: ")

        ingredient_searched_index = int(ingredient_searched_num) - 1

        search_ingredient = all_ingredients_list[ingredient_searched_index][1]

        print("\nYou selected the ingredient: ", search_ingredient)
    except:
        print("An unexpected error occurred. Please pick a number from the list.")

    else:
        print("\nThe recipe(s) below contain the selected ingredient: ")
        print("\n---------------------------------------------------")
        # searches for rows in table that contain search_ingredient
        cursor.execute('SELECT * FROM Recipes WHERE ingredients LIKE %s',
                       ('%' + search_ingredient + '%', ))

        # displays data from each recipe found
        results_recipes_with_ingredient = cursor.fetchall()
        for row in results_recipes_with_ingredient:
            print("\nID: ", row[0])
            print("Name: ", row[1])
            print("Ingredients: ", row[2])
            print("Cooking Time: ", row[3])
            print("Difficulty: ", row[4])


def update_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_update_id = int((
        input("Enter the ID of the recipe you would like to update: ")))
    # user inputs the specific column they want updated
    column_for_update = str(input(
        "\nEnter what data you would like to update between name, cooking time, and ingredients: "))
    updated_value = (input("\nWhat would you like the new value to be?: "))
    print("Choice: ", updated_value)

    if column_for_update == "name":
        cursor.execute('UPDATE Recipes SET name = %s WHERE id = %s',
                       (updated_value, recipe_update_id))
        print("Value updated.")

    elif column_for_update == "cooking time":
        cursor.execute('UPDATE Recipes SET cooking_time = %s WHERE id = %s',
                       (updated_value, recipe_update_id))
        print("Value updated.")
    # cooking time changes so difficulty must be recalibrated
    cursor.execute('SELECT * FROM Recipes WHERE id = %s', (recipe_update_id))
    result_recipe_update = cursor.fetchall()

    name = result_recipe_update[0][1]
    recipe_ingredients = tuple(result_recipe_update[0][2].split(','))
    cooking_time = result_recipe_update[0][3]

    updated_difficulty = calculate_difficulty(cooking_time, recipe_ingredients)
    print("Updated difficulty: ", updated_difficulty)
    cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s',
                   (updated_difficulty, recipe_update_id))
    print("Value updated.")

    if column_for_update == "ingredients":
        cursor.execute('UPDATE Recipes SET ingredients = %s WHERE id = %s',
                       (updated_value, recipe_update_id))

    cursor.execute('SELECT * FROM ingredients WHERE id = %s',
                   (recipe_update_id, ))
    result_recipe_update = cursor.fetchall()

    print("result_recipe_update: ", result_recipe_update)

    name = result_recipe_update[0][1]
    recipe_ingredients = tuple(result_recipe_update[0][2].split(','))
    cooking_time = result_recipe_update[0][3]
    difficulty = result_recipe_update[0][4]

    updated_difficulty = calculate_difficulty(cooking_time, recipe_ingredients)
    print("Updated difficulty: ", updated_difficulty)
    cursor.execute('UPDATE Recipes SET difficulty = %s WHERE id = %s',
                   (updated_difficulty, recipe_update_id))
    print("Value updated.")

    conn.commit()


def delete_recipe(conn, cursor):
    view_all_recipes(conn, cursor)
    recipe_deletion_id = (
        input("\nEnter the ID of the recipe you would like to delete: "))
    # deletes corresponding recipe from results
    cursor.execute('DELETE FROM Recipes WHERE id = (%s)', recipe_deletion_id)

  # commits data to database
    conn.commit()
    print("\nRecipe successfully deleted from database.")


def view_all_recipes(conn, cursor):
    print("\nAll recipes are displayed below: ")
    print("---------------------------------")
  # stores list of recipes into a variable called results
    cursor.execute('SELECT * FROM Recipes')
    results = cursor.fetchall()

    # displays data from each recipe
    for row in results:
        print("\nID: ", row[0])
        print("Name: ", row[1])
        print("Ingredients: ", row[2])
        print("Cooking Time: ", row[3])
        print("Difficulty: ", row[4])


# calls main_menu() function
main_menu(conn, cursor)
