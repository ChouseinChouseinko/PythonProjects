def add_task(task):
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')
    print(f"Task added: + {task}")


def view_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if not tasks:
            print("No task in the txt file")
        else:
            print("\nYour Tasks: ")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks founded sir")


def delete_task(task_number):
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open('tasks.txt', 'w') as file:
                file.writelines(tasks)
            print(f"Deleted task: {removed_task.strip()}")
        else:
            print("Invalid Task Number")
    except FileNotFoundError:
        print("No tasks to delete.")


def main():
    while True:
        print("\n This is your To-do List app")
        print("1. Add a task")
        print("2. Let's see your tasks")
        print("3. Remove tasks that you don't need")
        print("4. Exit from the script")

        answer = input("Select an option: ")

        if answer == '1':
            task = input("Enter the task please: ")
            add_task(task)
        elif answer == '2':
            view_tasks()
        elif answer == '3':
            view_tasks()
            try:
                task_number = int(input(
                    "What's the number of the task that you want to remove: "))

                delete_task(task_number)
            except ValueError:
                print("You entered invalid input. Please enter an invalid number ")
        elif answer == '4':
            print("Good Bye sir")
            break
        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()
