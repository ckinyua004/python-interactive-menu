import random
import time

def calculator():
    print("Welcome to the calculator")
    num1 = int(input("Enter thr first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation: ")

    if operation == "+":
        print(f"Results: {num1} + {num2}")
    elif operation == "-":
        print(f"Results: {num1} - {num2}")
    elif operation == "*":
        print(f"Results: {num1} * {num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Results: {num1} / {num2}")
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation !!!!!")

def temperature_converter():
    print("Temperature Converter")
    temp = int(input("Enter the temperature: "))
    unit = input("Enter the unit (C/F): ").upper()

    if unit == "C":
        print(f"Results: {temp} C = {temp * 9/5 + 32} F")
    elif unit == "F":
        print(f"Results: {temp} F = {(temp - 32) * 5/9} C")
    else:
        print("Invalid unit !!!!!")

def age_calculator():
    print("Age Calculator")
    birth_year = int(input("Enter the birth year: "))
    current_year = int(input("Enter the current year: "))

    if current_year >= birth_year:
        print(f"Results: Your age is {current_year - birth_year}")
    else:
        print("Invalid year !!!!!")

def even_odd_checker():
    print("Even odd checker")
    num = int(input("Enter the number: "))
    if num % 2 == 0:
        print("Results: Even number")
    else:
        print("Results: Odd number")

def guess_number_game():
    print("Guess the number game")
    number = random.randint(1,10)
    while True:
        guess = int(input("Guess the number between 1 and 10: "))
        if guess == number:
            print("Congratulations, you guessed the number")
            break
        elif guess < number:
            print("Try again, guess higher")
        else:
            print("Try again, guess lower")

def multiplication_table():
    print("Multiplication table.")
    num = int(input("Enter the number: "))
    for i in range(1,11):
        print(f"{num} x {i} = {num * i}")

def countdown_timer():
    print("Countdown timer")
    seconds = int(input("Enter the number of seconds: "))
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Time's up")

def to_do_list():
    tasks = []
    while True:
        print("\nTo-Do List:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)

        elif choice == "2":
            task = input("Enter the task to remove: ")
            if task in tasks:
                tasks.remove(task)
            else:
                print("Task not found")

        elif choice == "3":
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif choice == "4":
            break

while True:
    print("\nPython Utility Hub")
    print("1. Calculator")
    print("2. Temperature Converter")
    print("3. Age Calculator")
    print("4. Even or Odd Checker")
    print("5. Guess the Number Game")
    print("6. Multiplication Table")
    print("7. Countdown Timer")
    print("8. To-Do List")
    print("9. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculator()
    if choice == "2":
        temperature_converter()
    if choice == "3":
        age_calculator()
    if choice == "4":
        even_odd_checker()
    if choice == "5":
        guess_number_game()
    if choice == "6":
        multiplication_table()
    if choice == "7":
        countdown_timer()  
    if choice == "8":
        to_do_list()
    if choice == "9": 
        print("Goodbye")
        break
    else:
        print("Invalid option")

input("/nPress Enter to continue...")