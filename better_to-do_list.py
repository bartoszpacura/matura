# Modyfikuję to-do list, którą została przedstawiona w tym filmie: https://youtu.be/BBu6ZoAHIwI?t=6624
import itertools
import os.path

tasks = {}


def how_many():
    length = len(tasks) - 1
    return length


def show_tasks():
    for task in tasks:
        print(str(tasks[task]) + " [" + str(task) + "]")


def add_task():
    task = input("Enter the content of the task: ")
    a = how_many() + 1
    tasks[str(a)] = task
    print("\nThe task has been added\n")


def delete_task():
    element = input("Enter the name of the task you want to delete: ")
    try:
        tasks.pop(element)
        print("\nThe task has been successfully deleted\n")
    except KeyError:
        print("\nThis task doesn't exist\n")


def autosave(save_global):
    save = save_global

    if save is False:
        turn_off = input("Autosave is turn off. If you want to turn it on enter 'turn on' if not enter 'no': ")
        print()
        if turn_off == "turn on":
            return True
        elif turn_off == "no":
            print("The settings have not been changed")
            print()
            return save
        else:
            print("Invalid value")
            print()
            return save

    elif save is True:
        turn_on = input("Autosave is turn on. If you want to turn it off enter 'turn off' if not enter 'no': ")
        print()
        if turn_on == "turn off":
            return False
        elif turn_on == "no":
            print("The settings have not been changed")
            print()
            return save
        else:
            print("Invalid value")
            print()
            return save


def save_tasks(name_f):
    file = open(name_f, "w")
    for task in tasks:
        a = tasks[task]
        file.write(task + "\n" + a + "\n")
    file.close()


def save_tasks_to_file():
    answer = input("If you want to save tasks in an existing file check 1 or create a new file (check 2): \n")
    if answer == "1":
        file_name = input("Enter the name of the file: ")
        m = os.path.isfile("./" + file_name)
        if m is True:
            print("\nThe tasks have been successfully saved\n")
            save_tasks(file_name)
        else:
            print("\nThe file was not found\n")

        return file_name

    elif answer == "2":
        file_name = input("Enter the name of the new file: ")
        save_tasks(file_name)
        print("\nThe tasks have been successfully saved the new file" + str(file_name))

        return file_name

    else:
        print()
        print("Invalid value")
        print()


def save_after_exit(name, optional_s):
    if name != "" and optional_s is True:
        save_tasks(name)
    elif name == "":
        if os.path.isfile("./" + "new_save.txt") is False:
            save_tasks("new_save.txt")
        else:
            for number in itertools.count(start=2):
                if os.path.isfile("./" + "new_save_" + str(number) + ".txt") is False:
                    save_tasks("new_save_" + str(number) + ".txt")
                    break
                else:
                    continue


def load_tasks_from_file():
    file_name = input("Enter the name of the file: ")

    key = 0
    value = 0

    try:
        file = open(file_name, "r")
        f = file.readlines()
        count = 0
        for line in f:
            if count % 2 == 0:
                key = line.strip("\n")
            elif count % 2 != 0:
                value = line.strip("\n")

            tasks[key] = value
            count += 1

        file.close()
        print("\nThe content of the file has been loaded successfully\n")

    except FileNotFoundError:
        print("\nThe file was not found\n")


def show_menu():
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Save changes to file")
    print("5. Load changes from file")
    print("6. Autosave")
    print("7. Exit")


show_menu()
user_choice = 1
name_of_the_file = ""
auto_s = False

while True:
    try:
        print()
        user_choice = int(input("Choose number: "))
        print()

        if user_choice == 1:
            show_tasks()
            show_menu()

        elif user_choice == 2:
            add_task()
            show_menu()

        elif user_choice == 3:
            delete_task()
            show_menu()

        elif user_choice == 4:
            name_of_the_file = save_tasks_to_file()
            show_menu()

        elif user_choice == 5:
            load_tasks_from_file()
            show_menu()

        elif user_choice == 6:
            auto_s = autosave(auto_s)
            show_menu()

        elif user_choice == 7:
            save_after_exit(name_of_the_file, auto_s)
            print("Exit")
            break

        elif user_choice <= 0 or user_choice >= 7:
            print("Invalid Value!")
            print()
            show_menu()

    except ValueError:
        print()
        print("Invalid value")
        print()
        show_menu()
