import sys
class List:
    def __init__(self, item=None):
        # Inicializar a lista com o item
        self.Slist = []
        self.add_item(item)

    # Add string to list
    def add_item(self, item):
        self.Slist.append(item)
    
    # Remove string from list
    def remove(self):
        value = int(input("Remove item using name [1]\n"
                          "Remove item using index [2]\n"
                          "Insert: "))
        while value not in [1,2]:
            value = int(input("Pleas insert [1] or [2]: "))

        # Removing with name (key)
        if value == 1:
            remove = input("What you want to remove? ")
            if remove in self.Slist:
                self.Slist.remove(remove)
                print("Item removed!")
            else:
                print("Could not find the item :(")
        # Removing with position (index)
        elif value == 2:
            value = int(input("Witch index do you want to remove? "))
            if value-1 in range(len(self.Slist)):
                self.Slist.pop(value-1)
                print("Index removed with sucess!")
            else:
                print("Index invalid!")

    def show(self):
        print("Your list is composed by: \n")
        for i in range(len(self.Slist)):
            print(f"- {self.Slist[i]}")