# Personal Mini-Toolkit
# A simple program containing three useful tools.

print("========================================")
print("       PERSONAL MINI-TOOLKIT")
print("========================================")
print("Welcome to my Personal Mini-Toolkit!")
print("Choose a tool from the menu below.")

# This list stores all the tasks added by the user.
tasks = []

while True:
    print("\n========================================")
    print("1. To-Do List")
    print("2. Simple Calculator")
    print("3. Number Checker")
    print("4. Quit")
    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        # To-Do List: allows the user to add and view tasks.
        while True:
            print("\n--- TO-DO LIST ---")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Return to main menu")

            todo_choice = input("Choose an option: ")

            if todo_choice == "1":
                task = input("Enter a task: ")
                tasks.append(task)
                print(f"Task '{task}' has been added!")

            elif todo_choice == "2":
                if len(tasks) == 0:
                    print("Your task list is empty.")
                else:
                    print("\nYour tasks:")
                    for number, task in enumerate(tasks, start=1):
                        print(f"{number}. {task}")

            elif todo_choice == "3":
                print("Returning to the main menu.")
                break

            else:
                print(f"Sorry, '{todo_choice}' is not a valid option.")

    elif choice == "2":
        # Simple Calculator: performs basic mathematical operations.
        print("\n--- SIMPLE CALCULATOR ---")

        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))

            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            operation = input("Enter your choice: ")

            if operation == "1":
                result = first_number + second_number
                print(f"The answer is: {result}")

            elif operation == "2":
                result = first_number - second_number
                print(f"The answer is: {result}")

            elif operation == "3":
                result = first_number * second_number
                print(f"The answer is: {result}")

            elif operation == "4":
                if second_number == 0:
                    print("Sorry, you cannot divide by zero.")
                else:
                    result = first_number / second_number
                    print(f"The answer is: {result}")

            else:
                print(f"Sorry, '{operation}' is not a valid operation.")

        except ValueError:
            print("Please enter numbers only.")

    elif choice == "3":
        # Number Checker: checks whether a number is positive, negative, or zero.
        print("\n--- NUMBER CHECKER ---")

        try:
            number = float(input("Enter a number: "))

            if number > 0:
                print(f"{number} is a positive number.")

            elif number < 0:
                print(f"{number} is a negative number.")

            else:
                print(f"{number} is zero.")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using my Personal Mini-Toolkit!")
        break

    else:
        print(f"Sorry, '{choice}' is not a valid choice. Please choose 1, 2, 3, or 4.")