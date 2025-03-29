import os
import datetime

os.chdir(r"C:\AMG ARS")

def clear_screen():
    # Clear screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    error_message = ""
    while True:
        clear_screen()
        today = datetime.datetime.today().strftime("%d - %B - %Y")
        
        print("=" * 60)
        print("        Welcome to AMG's Airline Reservations System")
        print("=" * 60)
        print("                        Main Menu")
        print("=" * 60)
        print("Date Today:")
        print(today)
        print("=" * 60)
        print("Please choose the corresponding options below:\n")
        print(" 1. Display All Flight Schedules")
        print(" 2. Search Flight Schedules Schedules")
        print(" 3. Membership Registration")
        print(" 4. Login as Admin")
        print(" 5. Login as Registered user")
        print(" 6. Exit\n")
        
        if error_message:
            print(error_message + "\n")
        
        option = input(" Enter your option: ")
        
        if option == '1':
            display_upcoming_schedules()
        elif option in ['2', '3', '4', '5', '6']:
            clear_screen()
            print(f"You selected option {option}. Loading...\n")
            break  # Proceed to corresponding functionality
        else:
            error_message = "Invalid input! Please enter a number between 1 and 6."

def display_upcoming_schedules():
    clear_screen()
    print("=" * 80)
    print("                           Upcoming Flight Schedules")
    print("=" * 80)
    print("{:<12} {:<8} {:<8} {:<20} {:<20} {:<6}".format(
        "Flight No", "From", "To", "Departure", "Return", "Price"))
    print("-" * 80)

    try:
        with open("flights.txt", "r") as file:
            lines = file.readlines()
            if len(lines) <= 1:
                print("No flight schedules available.\n")
            else:
                for line in lines[1:]:  # Skip header
                    data = line.strip().split(",")
                    print("{:<12} {:<8} {:<8} {:<20} {:<20} {:<6}".format(*data))
    except FileNotFoundError:
        print("\nError: flights.txt not found.\n")
        print("Current Working Directory:", os.getcwd())  # Prints the current directory for debugging
        print("Files in directory:", os.listdir()) # Prints files in current directory for debuging
    
    input("\nPress Enter to return to the main menu...")

display_main_menu()
