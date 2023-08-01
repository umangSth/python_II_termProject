import time
import random
import os

from Check import Check as ck
from Quiz import quiz
from Users.User_Auth import session


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_and_prompt(message):
    # print("\n" * 50)
    # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # Move the cursor to the top
    print("\033[1;1H", end="")

    # Display the prompt
    print(message, end="")


def display_welcome_message(username):
    clear_and_prompt("\n__________________________________"
                     f"\nWelcome {username}, to Test your knowledge"
                     "\n__________________________________\n")


def prompt_for_action():
    print("Please select an option:")
    print("1. Take a Test")
    print("2. Test History")
    print("3. Logout")
    choice = input("Enter your choice: ")
    return choice


def main_cli_loop():
    while True:
        current_user = session()
        display_welcome_message(current_user[1])
        choice = prompt_for_action()
        if choice == '1':
            # code for the Test function
            quiz_view()
        elif choice == '2':
            # code for the Test History
            quiz_history_view()
        elif choice == '3':
            print("Good bye!!")
            break
        else:
            print("Invalid choice. Please try again!!")


def quiz_view():
    current_user = session()
    print("Your test will start now")
    time.sleep(2)
    questions = quiz.display_question()
    total_correct = 0

    if not questions:
        print("No questions found for the quiz.")
        return
    q_no = 1
    for question in questions:

        q_id, q_text, ans_1, ans_2, ans_3, ans_4 = question
        options = [ans_1, ans_2, ans_3, ans_4]
        random.shuffle(options)

        print(f"\nQuestion {q_no}: {q_text}")
        print("Options:")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = ck.check_answer_input(input("Enter the number of your answer (1-4): "))
        if ck.is_answer_correct(q_id, options[user_answer - 1]):
            total_correct += 1
        q_no += 1
    user_id = current_user[0]
    quiz.display_score_message(total_correct)
    quiz.upload_score(user_id, total_correct)


def quiz_history_view():
    current_user = session()
    user_id = current_user[0]

    quiz_history = quiz.get_quiz_history(user_id)

    if not quiz_history:
        print("No quiz history found for the current user.")
    else:
        print(f"\nQuiz History for {current_user[1]}:")
        print("----------------------------------------")
        q_no = 1
        total_score = 0
        scores = []
        for quiz_record in quiz_history:
            quiz_id, _, score, date = quiz_record
            print(f"Quiz No: {q_no}, Score: {score}, Date: {date}")
            q_no += 1
            total_score += score
            scores.append(score)
        print(f"Average score: {total_score/(q_no-1)}")
        min_score, max_score = quiz.get_high_low_score(scores)
        print(f"Your highest score is: {max_score} and lowest score is: {min_score}")
        time.sleep(2)

    return 0

