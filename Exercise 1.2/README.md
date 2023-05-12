# README File for Python Exercise 1.2

## Task
Create a structure called **all_recipes** that can contain individual recipes that have the following characteristics:
+ **name (str)**: Contains the name of the recipe
+ **cooking_time (int)**: Contains cooking time in minutes
+ **ingredients (list)**: Contains a number of ingredients of the string type 

### Methodology:
The data structure chosen for this exercise is the **dictionaries** data structure for a number of reasons.  Dictionaries are very flexible and easily modified, which I anticipate being a useful trait as the achievement progress and additional data is required to be added to the structure.  Dictionaries can also contain multiple data types, which is essential for this structure, as it utilizes strings to store the **Name** and individual **Ingredients** of the recipes, integers for the **Cooking Times** and lists for the **Ingredients** component as well.  Mutability will be key here as the recipes are updated as well.

**all_recipes = [ ]**

I decided to use the **list** structure type for the outer structure for the dictionaries because they can be sequential (a requirement) as well as easily containing multiple recipes that can be altered easily.

