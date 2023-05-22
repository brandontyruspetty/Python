class ShoppingList(object):
    def __init__(self, list_name):
        shopping_list = []
        self.list_name = list_name
        self.shopping_list = shopping_list

    def add_item(self, item):
        self.item = item
        if item in self.shopping_list:
            print("Item already in shopping list")
        else:
            self.shopping_list.append(item)
            print("Item added to list")

    def remove_item(self, item):
        self.item = item
        if item in self.shopping_list:
            self.shopping_list.remove(item)
        else:
            print("Item not on list")

    def view_list(self):
        print("Shopping List: ", self.list_name)
        print("------------------------------")
        for item in self.shopping_list:
            print(item)
