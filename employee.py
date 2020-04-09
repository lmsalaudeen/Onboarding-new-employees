import random
import string


def input_details():
    first_name = input("Please enter first name: ").lower()
    last_name = input("Please enter last name: ").lower()
    email = input("Please enter email address: ")
    employee_details = [first_name, last_name, email]
    return employee_details


def gen_password(employee_details):
    characters = string.ascii_letters
    random_string = ''.join(random.choice(characters) for i in range(5))

    random_password = (employee_details[0][0:2] + employee_details[1][-2:] + random_string)

    return random_password

start = True
all_employees = []

while start:
    employee_details = input_details()
    password = gen_password(employee_details)
    print(f"Your generated password is: {password}")

    # Ask if password is okay

    password_ok = input(f'Do you like this password: {password}? If yes, enter "Yes", if no enter "No" ')

    # password acceptance

    password_loop = True
    while password_loop:
        # if generated password is accepted
        if password_ok == "yes".lower():
            employee_details.append(password)
            all_employees.append(employee_details)
            # break out of password loop
            password_loop = False

        # if generated password is not accepted

        elif password_ok == "no".lower():
            chosen_password = input("Please enter your desired password (must be longer than or equal to 7 characters): ")

            # password length check
            password_length = True
            while password_length:
                if len(chosen_password) >= 7:
                    employee_details.append(chosen_password)
                    all_employees.append(employee_details)

                    # break out of password length and password acceptance loop
                    password_length = False
                    password_loop = False

                # if password is less than 7 characters

                else:
                    print('Your password is less than 7 characters')

                    chosen_password = input("Please enter your desired password (must be longer than or equal to 7 characters): ")

        # if user does not enter yes or no
        else:
            print('Please enter "Yes or No"')
            password_ok = input(f'Do you like this password: {password}? If yes, enter "Yes", if no enter "No" ')

    # new employee details?

    new_employeeDetails = input('Would you like to enter the details of a new employee? (reply with Yes or No) ')

    #new employee details loop
    new_employee_loop = True
    while new_employee_loop:
        if new_employeeDetails == "no".lower():
            new_employee_loop = False
            start = False


            # print employee details prompt
            print_details_prompt = input('Would you like to view the details of all employees entered so far? (reply with Yes or No) ')

            # print employee details loop
            print_loop = True
            while print_loop:
                if print_details_prompt == "yes".lower():
                    for item in all_employees:
                        print(item)
                        print_loop = False

                elif print_details_prompt == "no".lower():
                    print_loop = False

                else:
                    print('Please enter "Yes" or "No"')
                    print_details_prompt = input('Would you like to view the details of all employees entered so far? (reply with Yes or No) ')

            print('Thank you for using this program. Bye!')

        elif new_employeeDetails == "yes".lower():
            new_employee_loop = False
            start = True

        else:
            print('Please enter "Yes or No"')
            new_employeeDetails = input('Would you like to enter the details of a new employee? (reply with Yes or No) ')
            new_employee_loop = True




