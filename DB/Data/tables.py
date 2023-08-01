Tables = {
    'users': """
        CREATE TABLE users(
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            user_name VARCHAR(50) UNIQUE,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(50),
            password VARCHAR(50)
        )
    """,
    'questions': """
    CREATE TABLE questions(
            q_id INT AUTO_INCREMENT PRIMARY KEY,
            question VARCHAR(150),
            answer_1 VARCHAR(30),
            answer_2 VARCHAR(30),
            answer_3 VARCHAR(30),
            answer_4 VARCHAR(30)
        )
    """,
    'correct_answer': """
    CREATE TABLE correct_answers(
            ans_id INT AUTO_INCREMENT PRIMARY KEY,
            q_id INT,
            answer VARCHAR(30),
            FOREIGN KEY (q_id) REFERENCES questions(q_id)
        )            
    """,
    'quiz_results': """
      CREATE TABLE quiz_results(
            quiz_id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            score INT,
            date DATE,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        ) 
    """
}