def display_menu():
    print("Shopping list manager")
    print("1. add items")
    print("2. remove items")
    print("3. view items")
    print("4. Exit")
def main():
    shopping_list =[]
    display_menu()
    while True:
        choice = input("Enter your choice number:")
        if choice == "1":
             new_item = input("Enter the new item to be added:")
             shopping_list.append(new_item)
        elif choice == "2":
            rem_item = input("Enter the item to remove:")
            if rem_item in shopping_list:
                shopping_list.remove(rem_item)
            else:
                print("the item isn't available")
        elif choice == "3":
            if shopping_list:
                for i, item in enumerate(shopping_list, start= 1):
                    print(f"{i}. {item}")
            else:
                print("the list is empty:")
        elif choice == "4":
            break
        else:
            print("invalid choice")
main()