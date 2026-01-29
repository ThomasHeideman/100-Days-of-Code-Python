from requests import get
from html import unescape
# from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


url = "https://opentdb.com/api.php?amount=20&difficulty=easy&type=boolean"
response = get(url)
response.raise_for_status()
data = response.json()
question_data = data["results"]
question_bank = []

for question in question_data:
    question_text = unescape(question["question"])
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_questions():
    new_quiz.next_question()

print("You've completed the quiz!")
print(f"Your total score was {new_quiz.current_score}/{len(question_bank)}")
