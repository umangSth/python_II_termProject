from Users import User_Auth, User_Res
from Check import Check as ck
import time


def display_welcome_message():
    print("\n__________________________________")
    print("Welcome to to Test your knowledge")
    print("__________________________________")


def prompt_for_action():
    print("Please select an option:")
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    choice = input("Enter your choice: ")
    return choice


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


def login_view():
    while True:
        user_name = ck.Check_String(input("Enter your User name: "))
        response = User_Auth.user_login(user_name)
        if response == 0:
            print("No, user found! Register to access the application.")
            time.sleep(2)
            main_cli_loop()
            break
        response = password_view(user_name)
        while response == -1:
            print("Invalid Password, Try-again!!!")
            response = password_view(user_name)

        if response == 1:
            print("Login Successful.")
            #  here goes the calling to function that will do something after successful login
            break


def register_view():
    print("Welcome, to registration ")
    user_info = {'user_name': ck.Check_Username(input("Enter your user name: ")),
                 'first_name': ck.Check_String(input("Enter your First name: ")),
                 'last_name': ck.Check_String(input("Enter your Second name: ")),
                 'email': ck.Check_Email(input("Enter your email:")),
                 'password': ck.Check_Password(input("Enter the password: "))}
    User_Res.user_registration(user_info)


def password_view(user_name):
    password = ck.Check_String(input("Enter your password: "))
    response = User_Auth.user_password_chk(user_name, password)
    return response
