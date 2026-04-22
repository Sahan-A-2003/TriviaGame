import random

questions = {
    "What is the comment syntax for Python?": "#",
    "What is the file extension for Python?": ".py",
    "What is the comment syntax for JavaScript?": "//",
    "What is the file extension for JavaScript?": ".js",
    "What is the comment syntax for Java?": "//",
    "What is the file extension for Java?": ".java",
    "What is the comment syntax for C++?": "//",
    "What is the file extension for C++?": ".cpp",
    "What is the comment syntax for HTML?": "<!-- -->",
    "What is the file extension for HTML?": ".html",
    "What is the comment syntax for CSS?": "/* */",
    "What is the file extension for CSS?": ".css",
    "What is the comment syntax for PHP?": "// or #",
    "What is the file extension for PHP?": ".php",
    "What is the comment syntax for Ruby?": "#",
    "What is the file extension for Ruby?": ".rb",
    "What is the comment syntax for Go?": "//",
    "What is the file extension for Go?": ".go",
    "What is the comment syntax for Swift?": "//",
    "What is the file extension for Swift?": ".swift",
    "What is the comment syntax for SQL?": "--",
    "What is the file extension for SQL?": ".sql",
    "What is the comment syntax for Shell Script?": "#",
    "What is the file extension for Shell Script?": ".sh",
    "What is the comment syntax for TypeScript?": "//",
    "What is the file extension for TypeScript?": ".ts"
}

def python_trivia_game():
  questions_list = list(questions.keys())
  total_questions = 5
  score = 0

  select_question = random.sample(questions_list, total_questions)

  for idx, question in enumerate(select_question):
    print(f"{idx + 1}. {question}")
    user_answer = input("Your answer: ").lower().strip()
    correct_asnwer = questions[question]

    if user_answer == correct_asnwer.lower():
      print("Correct answer..\n")
      score += 1
    else:
      print(f"Wrong. The correct is: {correct_asnwer}. \n")

  print(f"Game over! You final score is: {score}/{total_questions}.")


python_trivia_game()