from Users import User_Auth, User_Res
from Check import Check as ck
from view import cli_home_view as home
import time
import os


# Clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Clear the screen and display a message
def clear_and_prompt(message):
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Move the cursor to the top
    print("\033[1;1H", end="")

    # Display the prompt
    print(message, end="")


# Display a welcome message
def display_welcome_message():
    clear_and_prompt("\n__________________________________"
                     "\nWelcome to Test your knowledge"
                     "\n__________________________________\n")


# Prompt the user for their action choice
def prompt_for_action():
    print("Please select an option:\n"
          "1. Login\n"
          "2. Register\n"
          "3. Quit\n")
    choice = input("Enter your choice: ")
    return choice


# Main loop for the command-line interface
def main_cli_loop():
    while True:
        display_welcome_message()
        choice = prompt_for_action()

        if choice == '1':
            #  code to display login view
            login_view()
        elif choice == '2':
            #  code to display register view
            register_view()
        elif choice == '3':
            print("Good bye!!")
            break
        else:
            print("Invalid choice. Please try again!!")
            time.sleep(2)


# Display the login view
def login_view():
    clear_screen()
    print("LOGIN\n")
    user_name = ck.Check_String(input("Enter your User name: "))
    response = User_Auth.user_login(user_name)
    if response == 0:
        print("No, user found! Register to access the application.")
        time.sleep(2)
        main_cli_loop()
        return
    response = password_view(user_name)
    while response == -1:
        print("Invalid Password, Try-again!!!")
        time.sleep(2)
        response = password_view(user_name)

    if response == 1:
        print("Login Successful.")
        # Call the function that handles actions after successful login
        time.sleep(1)
        home.main_cli_loop()


# Display the registration view
def register_view():
    clear_screen()
    print("Welcome, to Registration:\n ")
    user_info = {'user_name': ck.Check_Username(input("Enter your user name: ")),
                 'first_name': ck.Check_String(input("Enter your First name: ")),
                 'last_name': ck.Check_String(input("Enter your Second name: ")),
                 'email': ck.Check_Email(input("Enter your email:")),
                 'password': ck.Check_Password(input("Enter the password: "))}
    User_Res.user_registration(user_info)
    print("Registration successful!")
    time.sleep(2)


# Display the password entry view
def password_view(user_name):
    password = ck.Check_String(input("Enter your password: "))
    response = User_Auth.user_password_chk(user_name, password)
    return response
