# This is the same program that i have done before using the functions method but this time using the class method

class ToDoList():
    def __init__(self, tasks):
        self.tasks = []

    def print_menu(self):
        print("\n**** TODOLIST MENU***")
        print("1. View the list")
        print("2. Add a task in the list")
        print("3. Remove a task from list")
        print("4. Exit the program")

# Adding a method for getting choice from the user
    def get_choice(self):
        while True:
            # Create a variable name choioce for taking the input from the user
            choice = int(input("Please enter the choice of your own: "))
            valid_choices = ('1', '2', '3', '4')
            if choice not in valid_choices:
                print("Invalid choice")
            else:
                return choice

    def view_list(self):
        if not self.tasks:
            print("There is no task to be viewed\n")
            return

        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}.{task}")

    def add_list(self):
        while True:
            task = input(
                "Please enter the task you wanna add in the list:").strip()
            # Checking and adding in the list
            if len(task) != 0:
                self.tasks.append(task)
                break
            else:
                print("Please enter valid tasks in the list")

    def remove_task(self):
        self.display_tasks()

        if not self.tasks:
            return ("cannot remove as the list is empty")

        while True:
            try:
                task_number = int(
                    input("Please enter the task number you wanna remove from the list"))
                if 1 <= task_number <= len(self.tasks):
                    self.task.pop(task_number-1)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid choice of option")

    def main(self):
        while True:
            self.print_menu()
            choice = self.get_choice()

            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                break  # exit the program
