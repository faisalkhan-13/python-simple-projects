to_do_list = []


def add_item(item):
    to_do_list.append(item)


def view_list():
    print("To-do list:")
    for task in to_do_list:
        print(task)


def remove_item(index):
    to_do_list.pop(index)


def mark_completed(index):
    to_do_list[index] = to_do_list[index] + " (completed)"


while True:
    print("To-do list menu:")
    print("1. Add new item")
    print("2. View list")
    print("3. Remove item")
    print("4. Mark item as completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_item = input("Enter new item: ")
        add_item(new_item)
    elif choice == "2":
        view_list()
    elif choice == "3":
        item_index = int(input("Enter index of item to remove: "))
        remove_item(item_index)
    elif choice == "4":
        item_index = int(input("Enter index of item to mark as completed: "))
        mark_completed(item_index)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")

print("Goodbye!")
