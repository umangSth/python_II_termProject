Instruction:
First, run file Db.py to set the database schema and data. And, just run Main.py


Create a multiuser Python application that tests the knowledge of a certain topic. 
Your application should have at least 20 questions stored in database of your choice and each time the user starts the application, 5 of these questions are selected randomly. 
Before attempting a quiz, create an account for each user (if they do not have one) or allow them to login.
Quiz results of each user should be stored in database.
For every question, user should select one option out of four options presented.
When the user answers the fifth question, the application should display the user’s score and one of the following messages depending on their score. You should also display the percentage of the score (0%, 20%, 40%, 60%, 80% or 100%0.
1.	Score 0/5, 1/5 and 2/5 Message => “Please try again!”
2.	Score 3/5 Message => “Good job!”
3.	Score 4/5 Message => “Excellent work!”
4.	Score 5/5 Message => “You are a genius!”
The topic for the questions should be chosen carefully and all the questions should be meaningful. All the questions should be based on the same topic you have chosen.
If the score of the test is less than 50% (Option 1 see above) user should be given an option to retake the quiz.
Your application should allow the user to see all the scores of the quizzes taken so far.
You should also display the average score for all quizzes as well as the highest and lowest scores.
