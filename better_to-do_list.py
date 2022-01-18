# Modyfikuję to-do list, którą została przedstawiona w tym filmie: https://youtu.be/BBu6ZoAHIwI?t=6624
import itertools
import os.path

tasks = {}
completed_tasks = {}


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
        file_ext = input("Enter the file extension: ")
        file_name += file_ext
        save_tasks(file_name)
        print("\nThe tasks have been successfully saved the new file " + str(file_name))
        print()

        return file_name

    else:
        print()
        print("Invalid value")
        print()


def save_after_exit(name, optional_s):
    if name != "" and optional_s is True:
        save_tasks(name)
    elif name == "" and optional_s is True:
        if os.path.isfile("./" + "new_save.txt") is False:
            save_tasks("new_save.txt")
        else:
            for number in itertools.count(start=2):
                if os.path.isfile("./" + "new_save_" + str(number) + ".txt") is False:
                    save_tasks("new_save_" + str(number) + ".txt")
                    break
                else:
                    continue
    else:
        pass


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
        return file_name

    except FileNotFoundError:
        print("\nThe file was not found\n")
        return "fnf"


def list_of_tasks():
    print("Completed tasks: \n")
    if not completed_tasks:
        print("The list is empty\n")
    else:
        for k, v in sorted(completed_tasks.items()):
            print(v + " [" + k + "]")
        print()

    keys_1 = tasks.keys()
    keys_2 = completed_tasks.keys()
    difference = []
    difference = keys_1 - keys_2

    print("Uncompleted tasks: \n")
    if not completed_tasks:
        print("The list is empty\n")
    else:
        for k in sorted(difference):
            print(tasks[k] + " [" + k + "]")
        print()


def add_completed_task():
    task_to_list = input("Enter the task number to add the task it to the list of completed tasks, or enter 'no': ")
    ct_bool = False

    if str(task_to_list) == "no":
        print("\nNo tasks have been added to completed tasks\n")
    elif int(task_to_list) >= 0:
        for key in tasks.keys():
            if key == task_to_list:
                completed_tasks[key] = tasks[key]
                ct_bool = True
                print("\nThe task has been added to completed tasks\n")
                break
            else:
                continue
        if ct_bool is False:
            print("\nInvalid Value\n")
    else:
        print("\nInvalid Value\n")


def load_completed_tasks(name):

    key = 0
    value = 0

    try:
        file = open("completed tasks_" + name, "r")
        f = file.readlines()
        count = 0
        for line in f:
            if count % 2 == 0:
                key = line.strip("\n")
            elif count % 2 != 0:
                value = line.strip("\n")

            completed_tasks[key] = value
            count += 1
        file.close()
    except FileNotFoundError:
        pass


def save_completed_tasks_after_exit(name):
    if name == "":
        file = open("completed tasks.txt", "w")
        for task in completed_tasks:
            a = completed_tasks[task]
            file.write(task + "\n" + a + "\n")
        file.close()
    elif name != "" and name != "fnf":
        file = open("completed tasks_" + name, "w")
        for task in completed_tasks:
            a = completed_tasks[task]
            file.write(task + "\n" + a + "\n")
        file.close()
    elif name == "fnf":
        pass


def show_menu():
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Save changes to file")
    print("5. Load changes from file")
    print("6. Autosave")
    print("7. Completed tasks")
    print("8. Exit")


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
            name_of_the_file = load_tasks_from_file()
            load_completed_tasks(name_of_the_file)
            show_menu()

        elif user_choice == 6:
            auto_s = autosave(auto_s)
            show_menu()

        elif user_choice == 7:
            list_of_tasks()
            add_completed_task()
            list_of_tasks()
            show_menu()

        elif user_choice == 8:
            save_after_exit(name_of_the_file, auto_s)
            save_completed_tasks_after_exit(name_of_the_file)
            print("Exit")
            break

        elif user_choice <= 0 or user_choice >= 8:
            print("Invalid Value!")
            print()
            show_menu()

    except ValueError:
        print()
        print("Invalid value")
        print()
        show_menu()
