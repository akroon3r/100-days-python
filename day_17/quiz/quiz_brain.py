class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Question number {self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(answer=answer, correct_answer=current_question.answer)

    def check_answer(self,answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"Your current score is {self.score} out of {self.question_number}\n")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)