from List import List

def main():
    print("----------- Lista de compras -----------")
    Shopping_list = List()
    option = 0
    while option != 7:
        option = get_menu()
        match option:
            # Insert item
            case 1:
                value = input("Add: ")
                Shopping_list.add_item(value)
            # Remove item
            case 2:
                Shopping_list.remove()
            # Remove same items
            case 3:
                Shopping_list.remove_equals()
            # Sort list
            case 4:
                Shopping_list.sorting()
            # show the list
            case 5:
                print(Shopping_list)
            # Clear list
            case 6:
                Shopping_list.clear()
            #case 7: Stop Program

def get_menu():
    print()
    menu = int(input("Insert item [1]\n"
                     "Remove item [2]\n"
                     "Remove same items [3]\n"
                     "Sort the list [4]\n"
                     "Show list [5]\n"
                     "Clean list [6]\n"
                     "Stop program [7]\n\n"
                     "Insert a option: "))
    while menu not in [1, 2, 3, 4, 5, 6, 7]:
        menu = int(input("Insira alguma opção válida: "))
    return menu

if __name__ == "__main__":
    main()

