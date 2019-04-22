# Guess That Picture game


class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.correct = []
        self.incorrect = []
    
    def start(self):
        # Loop through questions and get answers for each
        for question in self.questions:
            self.printQuestion(question)
            response = self.handleInput(question)
            answer = question.get_answer(response - 1)
            if answer.is_correct:
                self.correct.append(question)
            else:
                self.incorrect.append(question)
        # Question taking over, display some results
        print('Thank you for taking the quiz, here are your results!')
        print('Correct: ' + str(len(self.correct)))
        print('Incorrect: ' + str(len(self.incorrect)))


    def printQuestion(self, question):
        printNow(question.question)
        for index, answer in enumerate(question.get_answer_values()):
            print("%s. %s" % (str(index + 1), answer))
    
    def handleInput(self, question):
        while True:
            response = requestString("Enter your answer")
            if int(response) in range(1, len(question.answers) + 1):
                response = int(response)
                print('\n')
                break
            else:
                print("Please enter a valid response")
        
        return response

class Question():
    def __init__(self, question, answers, image_path=''):
        self.question = question
        self.answers = answers
        self.scramble_image(image_path)

    def scramble_image(self, image_path):
        return
        # this should scramble the image using the path in the argument
        # self.scrambled_image =

    def get_answer_values(self):
        return [answer.value for answer in self.answers]

    def get_correct_answer(self):
        for answer in self.answers:
            if answer.is_correct:
                return answer

    def get_answer(self, index):
        return self.answers[index]


class Answer():
    def __init__(self, value, is_correct=False):
        self.value = value
        self.is_correct = is_correct


def game():
    quiz = Quiz([
        Question("Who dis?", [
            Answer(value="Andy"),
            Answer(value="Pooya"),
            Answer(value="Nicholas", is_correct=True),
        ]),
        Question("Who dis?", [
            Answer(value="Andy"),
            Answer(value="Pooya"),
            Answer(value="Nicholas", is_correct=True),
        ]),
        Question("Who dis?", [
            Answer(value="Andy"),
            Answer(value="Pooya"),
            Answer(value="Nicholas", is_correct=True),
        ])
    ])
    quiz.start()

game()