from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

if __name__ == '__main__':
    question_bank = []
    for item in question_data:
        new_question = Question(text=item["text"], answer=item["answer"])
        question_bank.append(new_question)

    quiz = QuizBrain(question_list=question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("The quiz is complete.")
    print(f"Your final score is {quiz.score} out of {quiz.question_number}")
