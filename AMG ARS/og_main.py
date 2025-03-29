import datetime

def separator():
    print("=" * 150)

def Main_Menu():
    separator()
    print('Welcome to Airline Reservations System (ARS) Main Menu!')
    separator()

    # Get today's date
    x = datetime.datetime.now()
    print("Date Today:")
    print(x.strftime('%d – %B'), '-', x.year)
    separator()

    print('Please choose the corresponding options below:')
    while True:
        option = int(input(
            '\n 1. Display every airline schedule'
            '\n 2. Finding airline'
            '\n 3. Membership registration'
            '\n 4. Login as admin'
            '\n 5. Login as registered user'
            '\n 6. Exit'
            '\n Enter your option: '
        ))

        if option == 1:
            display_all()  # Assuming this function is defined elsewhere
            break
        elif option == 2:
            search_data()  # Assuming this function is defined elsewhere
            break
        elif option == 3:
            registration()  # Assuming this function is defined elsewhere
            break
        elif option == 4:
            admin_login()  # Assuming this function is defined elsewhere
            break
        elif option == 5:
            user_login()  # Assuming this function is defined elsewhere
            break
        elif option == 6:
            Exit()  # Assuming this function is defined elsewhere
            break
        else:
            separator()
            print("Invalid input detected!")
            separator()
            print("Please choose the corresponding options below:")

def registration():
    # Implement registration logic here
    pass

def admin_login():
    # Implement admin login logic here
    pass

def user_login():
    # Implement user login logic here
    pass

def display_all():
    # Implement displaying all flights logic here
    pass

def search_data():
    # Implement search data logic here
    pass

def Exit():
    separator()
    print('Bye! Leaving...')
    separator()

def separator():
    print("=" * 150)

def add_flight_details():
    separator()
    with open('flight_details.txt', 'a') as f:
        flight_number = input('Enter flight number: ')
        departure = input('Enter departure location: ')
        destination = input('Enter destination: ')
        time = input('Enter time of departure: ')
        price = input('Enter price of ticket: ')
        f.write(f'{flight_number},{departure},{destination},{time},{price}\n')
    separator()
    print('Flight details successfully added.')
    separator()

def modifying_flight_rows():
    with open('flight_rows.txt', 'r') as flight_file:
        flight_data = [line.strip().split() for line in flight_file]

    separator()
    print('FLIGHT SCHEDULE')
    separator()

    while True:
        print('Please choose an option:')
        print('1. Change Flight number')
        print('2. Change Departure Date')
        print('3. Change Destination')
        print('4. Change Time')
        print('5. Change Price')
        print('6. Exit (Back to admin menu)')
        
        search = int(input('Option Number: '))
        
        if 1 <= search <= 5:
            for row in flight_data:
                with open('flight_rows.txt', 'r+') as towrite_file:
                    separator()
                    if search == 1:
                        newinput = input('Type in new flight number: ')
                        towrite_file.write(line.replace(row[2], newinput))
                    elif search == 2:
                        newinput = input('Type in new departure location: ')
                        towrite_file.write(line.replace(row[4], newinput))
                    elif search == 3:
                        newinput = input('Type in new destination: ')
                        towrite_file.write(line.replace(row[5], newinput))
                    elif search == 4:
                        newinput = input('Type in new time of departure: ')
                        towrite_file.write(line.replace(row[6], newinput))
                    elif search == 5:
                        newinput = input('Type in price of ticket: ')
                        towrite_file.write(line.replace(row[9], newinput))
                    print(f'Change for option {search} was successful!')
                    modifying_flight_rows()
        elif search == 6:
            display()
            break
        else:
            separator()
            print('Invalid input!')

def display():
    separator()
    while True:
        print('Please choose from the following options:')
        print('1. Scheduled Flights')
        print('2. Booked Flights/Tickets Sold')
        print('3. Logout (Exit)')
        choice = int(input('Enter your choice: '))
        
        if choice == 1:
            display_all()  # Assuming this function is defined elsewhere
            break
        elif choice == 2:
            booked_flights()  # Assuming this function is defined elsewhere
            break
        elif choice == 3:
            Exit()
            break
        else:
            print('Invalid choice. Choose again.')

def booked_flights():
    separator()
    with open("booked_flights.txt", 'r') as file:
        booked_flights_data = file.readlines()
        for i in range(len(booked_flights_data)):
            booked_flights_data[i] = booked_flights_data[i][:-1]
            print(booked_flights_data[i])
    separator()

def user_login():
    separator()
    print('Enter your login details:')
    user_username = input('Enter your name: ')
    user_password = input('Enter your password: ')

    with open('user_login_username.txt', 'r') as f0, open('user_login_password.txt', 'r') as f1:
        file_content0 = f0.read()
        file_content1 = f1.read()
        flag1 = 0
        flag0 = 0
        for x in file_content0.split('\n'):
            if user_username == x:
                flag0 = 1
                break
        for x in file_content1.split('\n'):
            if user_password == x:
                flag1 = 1
                break
        
        if flag1 == 1 and flag0 == 1:
            separator()
            print('Access Granted')
            separator()
            registered_user(user_username)
        else:
            print('Access Denied')
        separator()

def registered_user(user_username):
    separator()
    while True:
        print('Please choose the corresponding options:')
        print('1. Display My Profile')
        print('2. Book a flight')
        print('3. Modify My Profile')
        print('4. Online Check-In')
        print('5. Enquiries, Requests, and Feedback')
        print('6. Exit (Logout)')

        choice = int(input('Enter your choice: '))

        if choice == 1:
            display_userprofile(user_username)
            break
        elif choice == 2:
            flight_booking()
            break
        elif choice == 3:
            modify_userprofile(user_username)
            break
        elif choice == 4:
            online_check_in(user_username)
            break
        elif choice == 5:
            queries()
            break
        elif choice == 6:
            Exit()
            break
        else:
            print('Invalid choice. Choose again.')

def display_userprofile(user_username):
    separator()
    with open('MembershipRecords.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            if user_username in line:
                print(line)
                break
    separator()

def flight_booking():
    separator()
    with open('AirlineReservation.txt', 'r') as f1:
        print(f1.read())
    
    line_num = int(input('Enter line number of the flight you want to book: '))
    with open('AirlineReservation.txt', 'r') as f:
        file_data = f.readlines()
        line_num = line_num - 1
        print(f'Your selected flight: \n{file_data[line_num]}')

        with open('Booked_flights.txt', 'w') as f2:
            f2.writelines(file_data[line_num])
    f1.close()
    f.close()
    f2.close()
    separator()

def modify_userprofile(user_username):
    separator()
    count = 0
    with open('MembershipRecords.txt', 'r') as file:
        f = file.readlines()
        for line in f:
            count += 1
            if user_username in line:
                print(line)
                break
    
    with open('MembershipRecords.txt', 'r') as f1:
        file_data = f1.readlines()
        replacement = input('Enter replacement item in the same format as the above: ')
        count -= 1
        file_data[count] = replacement + '\n'
        with open('MembershipRecords.txt', 'w') as f:
            f.writelines(file_data)
    separator()

def online_check_in(user_username):
    option = input('Enter Y to confirm online check-in and N to decline: ')
    if option.lower() == 'y':
        count = 0
        with open('MembershipRecords.txt', 'r') as file:
            f = file.readlines()
            for line in f:
                count += 1
                if user_username in line:
                    line1 = line + ' Online Check-In'
                    with open('MembershipRecords.txt', 'r') as f1:
                        file_data = f1.readlines()
                        count -= 1
                        file_data[count] = line1 + '\n'
                        with open('MembershipRecords.txt', 'w') as f:
                            f.writelines(file_data)
        separator()
    elif option.lower() == 'n':
        registered_user(user_username)
    else:
        print('Invalid input. Please try again.')
        online_check_in(user_username)

def queries():
    queries1 = input('Enter your queries below: ')
    with open('queries.txt', 'a') as file:
        file.writelines('\n' + queries1)
    separator()

def Exit():
    separator()
    print('Bye! Leaving...')
    separator()

# Call the Main_Menu to start the program
Main_Menu()
