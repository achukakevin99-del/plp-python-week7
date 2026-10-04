# shopping_list.py
# Week 7 - Part B: Shopping List Manager

# 1. Start with an empty list
shopping_list = []

# 2. Loop to show the menu again and again
while True:
    choice = input("\nChoose an option (add / remove / show / done): ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()
        if item == "":
            print("You did not type anything.")
        else:
            shopping_list.append(item)
            print(f"'{item}' has been added.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()
        # Check with 'in' BEFORE removing so the program never crashes
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for item in shopping_list:
                print(item)

    elif choice == "done":
        print("Goodbye! Happy shopping!")
        break

    else:
        print("Invalid option. Please type add, remove, show or done.")
