# Guess That Picture game


class Question():
    def __init__(self, question, answers, image_path):
        self.question = question
        self.answers = answers
        scramble_image(image_path)

    def scramble_image(self, image_path):
        # this should scramble the image using the path in the argument
        # self.scrambled_image =

    def get_answer_values(self):
        return [answer.value for answer in self.answers]

    def get_correct_answer(self):
        return next((answer for answer in self.answers if answer.is_correct), None)


class Answer():
    def __init__(self, value, is_correct=False):
        self.value = value
        self.is_correct = is_correct


def game():
    question1 = Question("Who dis?", [
        Answer("Andy"),
        Answer("Pooya"),
        Answer("Nicholas", True),
    ])

    printNow(question1.question)
    for index, answer in enumerate(question1.get_answer_values()):
        print "%s. %s" % (str(index + 1), answer)
